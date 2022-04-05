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

import requests as rq
from bs4 import BeautifulSoup


def member_of():
    response = rq.get("https://graph.microsoft.com/beta/me/memberOf", 
    headers={'Authorization':'eyJ0eXAiOiJKV1QiLCJub25jZSI6Imhyam9vNDB1Z0llMVhfNlF1T0hFVWFfOHptQjJja0RzTVlVY08teUZnLWsiLCJhbGciOiJSUzI1NiIsIng1dCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyIsImtpZCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC85MDFjYjRjYS1iODYyLTQwMjktOTMwNi1lNWNkMGY2ZDlmODYvIiwiaWF0IjoxNjI5MzIwMTIxLCJuYmYiOjE2MjkzMjAxMjEsImV4cCI6MTYyOTMyNDAyMSwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFVUUF1LzhUQUFBQVIrc3JqZEhZUGNWb0t1TWtVQ1IxUHJsdm9iY2lzZXdmNlNySGdTUGl5QXU5MU4ydlpqTHJCc2NGOTZjMkxnbGZZS1NOMmZwcmlsZ1dSbFg2VTJqWTJ3PT0iLCJhbXIiOlsicHdkIiwibWZhIl0sImFwcF9kaXNwbGF5bmFtZSI6IkdyYXBoIEV4cGxvcmVyIiwiYXBwaWQiOiJkZThiYzhiNS1kOWY5LTQ4YjEtYThhZC1iNzQ4ZGE3MjUwNjQiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IkNhcmRvc28iLCJnaXZlbl9uYW1lIjoiQmFwdGlzdGUiLCJpZHR5cCI6InVzZXIiLCJpbl9jb3JwIjoidHJ1ZSIsImlwYWRkciI6Ijc4LjIwMS42Ni4xOTUiLCJuYW1lIjoiQmFwdGlzdGUgQ2FyZG9zbyIsIm9pZCI6Ijc1NmJkNmYzLWM5NDMtNGQ4Ni1hOTkxLTYxZjIzYmVkZjdjNyIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS0xNTUyNDM1Mjc3LTE1OTY0OTU3OTUtMzA4OTYxMzczMS00MjkwNiIsInBsYXRmIjoiOCIsInB1aWQiOiIxMDAzMjAwMTRBQTI1RkFGIiwicmgiOiIwLkFYUUF5clFja0dLNEtVQ1RCdVhORDIyZmhyWElpOTc1MmJGSXFLMjNTTnB5VUdSMEFDVS4iLCJzY3AiOiJHcm91cC5SZWFkLkFsbCBHcm91cC5SZWFkV3JpdGUuQWxsIG9wZW5pZCBwcm9maWxlIFVzZXIuUmVhZCBlbWFpbCIsInNpZ25pbl9zdGF0ZSI6WyJrbXNpIl0sInN1YiI6IlNKMVJLVFJ5dWp3TElxQkl4ZUt6TFZ0QU1pVElZSXRESEpqcFB1N3ZvS3MiLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiRVUiLCJ0aWQiOiI5MDFjYjRjYS1iODYyLTQwMjktOTMwNi1lNWNkMGY2ZDlmODYiLCJ1bmlxdWVfbmFtZSI6ImJhcHRpc3RlLmNhcmRvc29AZXBpdGVjaC5ldSIsInVwbiI6ImJhcHRpc3RlLmNhcmRvc29AZXBpdGVjaC5ldSIsInV0aSI6IjVUTWxqenNzRWtLMVkyaWJwUUJ0QUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfc3QiOnsic3ViIjoiU3o0eVNvbWUzUzRrTkJCT05QZjdoUl9Vd0lVMXpJRWpBQ3FZNmZENWJINCJ9LCJ4bXNfdGNkdCI6MTQxNzgwNDg4N30.cKcpWVn_KY5cVeu3gTHHfA5AjgaTHiKs-bo8m8JMJ27PImH4yJlTFWjVL5gw_KCcGMTgdyH3P1MkEsJ6GiCwMbVE2PG85hl8irfURSNGgyxq-IrtRmWfOWOd9sHrFn-QVteVwcL0q2UInFDaJIY33kJHCYdh6zbBzflDnDmVPXlPPSM0hTQWG8eMWNtgYxEIe6HJG9Ng27bn5Lzkl10XNc2HL5uwzNfYn6gq0PrT8RkVVMAr28AjcEW-Hb-yJTRraSywVOR2YAraug1Qp7UNIObhenMN_kbt8bpm3A7sT3SZC1U1IyyqGKlz_w4TDriqIuqdJi2ttxHIOgH9_CgyNg'})
    data = response.json()
    for team in data["value"]:
        # print("___________________")
        print(team["displayName"])
        print(team["id"])      
        print("___________________")
        tm = Teams(name=team["displayName"], team_id=team["id"])
        session.add(tm)
        session.commit()
        response1 = rq.get("https://graph.microsoft.com/beta/teams/" + team["id"] + "/channels",
        headers={'Authorization':'eyJ0eXAiOiJKV1QiLCJub25jZSI6Imhyam9vNDB1Z0llMVhfNlF1T0hFVWFfOHptQjJja0RzTVlVY08teUZnLWsiLCJhbGciOiJSUzI1NiIsIng1dCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyIsImtpZCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC85MDFjYjRjYS1iODYyLTQwMjktOTMwNi1lNWNkMGY2ZDlmODYvIiwiaWF0IjoxNjI5MzIwMTIxLCJuYmYiOjE2MjkzMjAxMjEsImV4cCI6MTYyOTMyNDAyMSwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFVUUF1LzhUQUFBQVIrc3JqZEhZUGNWb0t1TWtVQ1IxUHJsdm9iY2lzZXdmNlNySGdTUGl5QXU5MU4ydlpqTHJCc2NGOTZjMkxnbGZZS1NOMmZwcmlsZ1dSbFg2VTJqWTJ3PT0iLCJhbXIiOlsicHdkIiwibWZhIl0sImFwcF9kaXNwbGF5bmFtZSI6IkdyYXBoIEV4cGxvcmVyIiwiYXBwaWQiOiJkZThiYzhiNS1kOWY5LTQ4YjEtYThhZC1iNzQ4ZGE3MjUwNjQiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IkNhcmRvc28iLCJnaXZlbl9uYW1lIjoiQmFwdGlzdGUiLCJpZHR5cCI6InVzZXIiLCJpbl9jb3JwIjoidHJ1ZSIsImlwYWRkciI6Ijc4LjIwMS42Ni4xOTUiLCJuYW1lIjoiQmFwdGlzdGUgQ2FyZG9zbyIsIm9pZCI6Ijc1NmJkNmYzLWM5NDMtNGQ4Ni1hOTkxLTYxZjIzYmVkZjdjNyIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS0xNTUyNDM1Mjc3LTE1OTY0OTU3OTUtMzA4OTYxMzczMS00MjkwNiIsInBsYXRmIjoiOCIsInB1aWQiOiIxMDAzMjAwMTRBQTI1RkFGIiwicmgiOiIwLkFYUUF5clFja0dLNEtVQ1RCdVhORDIyZmhyWElpOTc1MmJGSXFLMjNTTnB5VUdSMEFDVS4iLCJzY3AiOiJHcm91cC5SZWFkLkFsbCBHcm91cC5SZWFkV3JpdGUuQWxsIG9wZW5pZCBwcm9maWxlIFVzZXIuUmVhZCBlbWFpbCIsInNpZ25pbl9zdGF0ZSI6WyJrbXNpIl0sInN1YiI6IlNKMVJLVFJ5dWp3TElxQkl4ZUt6TFZ0QU1pVElZSXRESEpqcFB1N3ZvS3MiLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiRVUiLCJ0aWQiOiI5MDFjYjRjYS1iODYyLTQwMjktOTMwNi1lNWNkMGY2ZDlmODYiLCJ1bmlxdWVfbmFtZSI6ImJhcHRpc3RlLmNhcmRvc29AZXBpdGVjaC5ldSIsInVwbiI6ImJhcHRpc3RlLmNhcmRvc29AZXBpdGVjaC5ldSIsInV0aSI6IjVUTWxqenNzRWtLMVkyaWJwUUJ0QUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfc3QiOnsic3ViIjoiU3o0eVNvbWUzUzRrTkJCT05QZjdoUl9Vd0lVMXpJRWpBQ3FZNmZENWJINCJ9LCJ4bXNfdGNkdCI6MTQxNzgwNDg4N30.cKcpWVn_KY5cVeu3gTHHfA5AjgaTHiKs-bo8m8JMJ27PImH4yJlTFWjVL5gw_KCcGMTgdyH3P1MkEsJ6GiCwMbVE2PG85hl8irfURSNGgyxq-IrtRmWfOWOd9sHrFn-QVteVwcL0q2UInFDaJIY33kJHCYdh6zbBzflDnDmVPXlPPSM0hTQWG8eMWNtgYxEIe6HJG9Ng27bn5Lzkl10XNc2HL5uwzNfYn6gq0PrT8RkVVMAr28AjcEW-Hb-yJTRraSywVOR2YAraug1Qp7UNIObhenMN_kbt8bpm3A7sT3SZC1U1IyyqGKlz_w4TDriqIuqdJi2ttxHIOgH9_CgyNg'})
        datachannels = response1.json()        
        #try:
        for channel in datachannels["value"]:    
            print("___________________")
            print(channel["displayName"])
            print(channel["id"])
            # print("___________________")
            chnl = Channels(channel_id=channel["id"], name=channel["displayName"], team_id=team["id"])
            session.add(chnl)
            session.commit()
            
            response2 = rq.get("https://graph.microsoft.com/beta/teams/" + team["id"] + "/channels/" + channel["id"] + "/messages",
            headers={'Authorization':'eyJ0eXAiOiJKV1QiLCJub25jZSI6Imhyam9vNDB1Z0llMVhfNlF1T0hFVWFfOHptQjJja0RzTVlVY08teUZnLWsiLCJhbGciOiJSUzI1NiIsIng1dCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyIsImtpZCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC85MDFjYjRjYS1iODYyLTQwMjktOTMwNi1lNWNkMGY2ZDlmODYvIiwiaWF0IjoxNjI5MzIwMTIxLCJuYmYiOjE2MjkzMjAxMjEsImV4cCI6MTYyOTMyNDAyMSwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFVUUF1LzhUQUFBQVIrc3JqZEhZUGNWb0t1TWtVQ1IxUHJsdm9iY2lzZXdmNlNySGdTUGl5QXU5MU4ydlpqTHJCc2NGOTZjMkxnbGZZS1NOMmZwcmlsZ1dSbFg2VTJqWTJ3PT0iLCJhbXIiOlsicHdkIiwibWZhIl0sImFwcF9kaXNwbGF5bmFtZSI6IkdyYXBoIEV4cGxvcmVyIiwiYXBwaWQiOiJkZThiYzhiNS1kOWY5LTQ4YjEtYThhZC1iNzQ4ZGE3MjUwNjQiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IkNhcmRvc28iLCJnaXZlbl9uYW1lIjoiQmFwdGlzdGUiLCJpZHR5cCI6InVzZXIiLCJpbl9jb3JwIjoidHJ1ZSIsImlwYWRkciI6Ijc4LjIwMS42Ni4xOTUiLCJuYW1lIjoiQmFwdGlzdGUgQ2FyZG9zbyIsIm9pZCI6Ijc1NmJkNmYzLWM5NDMtNGQ4Ni1hOTkxLTYxZjIzYmVkZjdjNyIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS0xNTUyNDM1Mjc3LTE1OTY0OTU3OTUtMzA4OTYxMzczMS00MjkwNiIsInBsYXRmIjoiOCIsInB1aWQiOiIxMDAzMjAwMTRBQTI1RkFGIiwicmgiOiIwLkFYUUF5clFja0dLNEtVQ1RCdVhORDIyZmhyWElpOTc1MmJGSXFLMjNTTnB5VUdSMEFDVS4iLCJzY3AiOiJHcm91cC5SZWFkLkFsbCBHcm91cC5SZWFkV3JpdGUuQWxsIG9wZW5pZCBwcm9maWxlIFVzZXIuUmVhZCBlbWFpbCIsInNpZ25pbl9zdGF0ZSI6WyJrbXNpIl0sInN1YiI6IlNKMVJLVFJ5dWp3TElxQkl4ZUt6TFZ0QU1pVElZSXRESEpqcFB1N3ZvS3MiLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiRVUiLCJ0aWQiOiI5MDFjYjRjYS1iODYyLTQwMjktOTMwNi1lNWNkMGY2ZDlmODYiLCJ1bmlxdWVfbmFtZSI6ImJhcHRpc3RlLmNhcmRvc29AZXBpdGVjaC5ldSIsInVwbiI6ImJhcHRpc3RlLmNhcmRvc29AZXBpdGVjaC5ldSIsInV0aSI6IjVUTWxqenNzRWtLMVkyaWJwUUJ0QUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfc3QiOnsic3ViIjoiU3o0eVNvbWUzUzRrTkJCT05QZjdoUl9Vd0lVMXpJRWpBQ3FZNmZENWJINCJ9LCJ4bXNfdGNkdCI6MTQxNzgwNDg4N30.cKcpWVn_KY5cVeu3gTHHfA5AjgaTHiKs-bo8m8JMJ27PImH4yJlTFWjVL5gw_KCcGMTgdyH3P1MkEsJ6GiCwMbVE2PG85hl8irfURSNGgyxq-IrtRmWfOWOd9sHrFn-QVteVwcL0q2UInFDaJIY33kJHCYdh6zbBzflDnDmVPXlPPSM0hTQWG8eMWNtgYxEIe6HJG9Ng27bn5Lzkl10XNc2HL5uwzNfYn6gq0PrT8RkVVMAr28AjcEW-Hb-yJTRraSywVOR2YAraug1Qp7UNIObhenMN_kbt8bpm3A7sT3SZC1U1IyyqGKlz_w4TDriqIuqdJi2ttxHIOgH9_CgyNg'})
            datamessage = response2.json()
            for message in datamessage["value"]:
                if message["from"] == None:
                    print("-")
                else:
                    print("___________________________________________________________________")
                    print(message["from"]["user"]["displayName"])
                    soup = BeautifulSoup(message["body"]["content"], 'html.parser')
                    print(soup.get_text())
                    msg = Messages(message_id=message["id"], author=message["from"]["user"]["displayName"], content=soup.get_text(), channel_id=channel["id"])
                    session.add(msg)
                    session.commit()
                                        
                    res = rq.get("https://graph.microsoft.com/beta/teams/" + team["id"] + "/channels/" + channel["id"] + "/messages/" + message["id"] + "/replies",
                    headers={'Authorization':'eyJ0eXAiOiJKV1QiLCJub25jZSI6Imhyam9vNDB1Z0llMVhfNlF1T0hFVWFfOHptQjJja0RzTVlVY08teUZnLWsiLCJhbGciOiJSUzI1NiIsIng1dCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyIsImtpZCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC85MDFjYjRjYS1iODYyLTQwMjktOTMwNi1lNWNkMGY2ZDlmODYvIiwiaWF0IjoxNjI5MzIwMTIxLCJuYmYiOjE2MjkzMjAxMjEsImV4cCI6MTYyOTMyNDAyMSwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFVUUF1LzhUQUFBQVIrc3JqZEhZUGNWb0t1TWtVQ1IxUHJsdm9iY2lzZXdmNlNySGdTUGl5QXU5MU4ydlpqTHJCc2NGOTZjMkxnbGZZS1NOMmZwcmlsZ1dSbFg2VTJqWTJ3PT0iLCJhbXIiOlsicHdkIiwibWZhIl0sImFwcF9kaXNwbGF5bmFtZSI6IkdyYXBoIEV4cGxvcmVyIiwiYXBwaWQiOiJkZThiYzhiNS1kOWY5LTQ4YjEtYThhZC1iNzQ4ZGE3MjUwNjQiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IkNhcmRvc28iLCJnaXZlbl9uYW1lIjoiQmFwdGlzdGUiLCJpZHR5cCI6InVzZXIiLCJpbl9jb3JwIjoidHJ1ZSIsImlwYWRkciI6Ijc4LjIwMS42Ni4xOTUiLCJuYW1lIjoiQmFwdGlzdGUgQ2FyZG9zbyIsIm9pZCI6Ijc1NmJkNmYzLWM5NDMtNGQ4Ni1hOTkxLTYxZjIzYmVkZjdjNyIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS0xNTUyNDM1Mjc3LTE1OTY0OTU3OTUtMzA4OTYxMzczMS00MjkwNiIsInBsYXRmIjoiOCIsInB1aWQiOiIxMDAzMjAwMTRBQTI1RkFGIiwicmgiOiIwLkFYUUF5clFja0dLNEtVQ1RCdVhORDIyZmhyWElpOTc1MmJGSXFLMjNTTnB5VUdSMEFDVS4iLCJzY3AiOiJHcm91cC5SZWFkLkFsbCBHcm91cC5SZWFkV3JpdGUuQWxsIG9wZW5pZCBwcm9maWxlIFVzZXIuUmVhZCBlbWFpbCIsInNpZ25pbl9zdGF0ZSI6WyJrbXNpIl0sInN1YiI6IlNKMVJLVFJ5dWp3TElxQkl4ZUt6TFZ0QU1pVElZSXRESEpqcFB1N3ZvS3MiLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiRVUiLCJ0aWQiOiI5MDFjYjRjYS1iODYyLTQwMjktOTMwNi1lNWNkMGY2ZDlmODYiLCJ1bmlxdWVfbmFtZSI6ImJhcHRpc3RlLmNhcmRvc29AZXBpdGVjaC5ldSIsInVwbiI6ImJhcHRpc3RlLmNhcmRvc29AZXBpdGVjaC5ldSIsInV0aSI6IjVUTWxqenNzRWtLMVkyaWJwUUJ0QUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfc3QiOnsic3ViIjoiU3o0eVNvbWUzUzRrTkJCT05QZjdoUl9Vd0lVMXpJRWpBQ3FZNmZENWJINCJ9LCJ4bXNfdGNkdCI6MTQxNzgwNDg4N30.cKcpWVn_KY5cVeu3gTHHfA5AjgaTHiKs-bo8m8JMJ27PImH4yJlTFWjVL5gw_KCcGMTgdyH3P1MkEsJ6GiCwMbVE2PG85hl8irfURSNGgyxq-IrtRmWfOWOd9sHrFn-QVteVwcL0q2UInFDaJIY33kJHCYdh6zbBzflDnDmVPXlPPSM0hTQWG8eMWNtgYxEIe6HJG9Ng27bn5Lzkl10XNc2HL5uwzNfYn6gq0PrT8RkVVMAr28AjcEW-Hb-yJTRraSywVOR2YAraug1Qp7UNIObhenMN_kbt8bpm3A7sT3SZC1U1IyyqGKlz_w4TDriqIuqdJi2ttxHIOgH9_CgyNg'})
                    comments = res.json()
                    for comment in comments["value"]:
                        if comment["from"] == None:
                            continue
                        else:
                            print("____" + comment["from"]["user"]["displayName"])
                            soup = BeautifulSoup(comment["body"]["content"], 'html.parser')
                            print("_______" + soup.get_text())
                            cmt = Replies(reply_id=comment["id"], content=soup.get_text(), message_id=message["id"])
                            session.add(cmt)
                            session.commit() 
                            
        #except Exception:
         #   pass
            

member_of()