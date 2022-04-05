import sqlite3
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
#from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


conn = sqlite3.connect('teams.db')

engine = create_engine('sqlite:///teams.db', echo = False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Teams(Base):
    __tablename__ = 'teams'
    
    id = Column(Integer, primary_key=True)
    team_id = Column(String())
    name = Column(String())
    children = relationship("Channels")

class Channels(Base):
    __tablename__ = 'channels'
    id = Column(Integer, primary_key=True)
    channel_id = Column(String())
    name = Column(String())
    team_id = Column(String(), ForeignKey('teams.team_id'))
    children = relationship("Messages")
    
class Messages(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    message_id = Column(String())
    author = Column(String())
    content = Column(String())
    channel_id = Column(String(), ForeignKey('channels.channel_id'))
    children = relationship("Replies")

class Replies(Base):
    __tablename__ = 'replies'
    id = Column(Integer, primary_key=True)
    reply_id = Column(String())
    content = Column(String())
    message_id = Column(String(), ForeignKey('messages.message_id'))


Base.metadata.create_all(engine)