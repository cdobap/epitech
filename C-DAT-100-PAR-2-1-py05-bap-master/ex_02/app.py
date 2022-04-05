from flask import Flask
from flask import request
import pandas as pd
import json

france = pd.read_csv("2020_french_house_pricing.csv")

def get_departments():
    dpt = france["Code departement"]
    df = pd.DataFrame(dpt)
    df_dpt = pd.DataFrame(df["Code departement"].unique())
    return df_dpt.to_json()

def get_towns():
    towns = france["Commune"]
    df = pd.DataFrame(towns)
    df_towns = pd.DataFrame(df["Commune"].unique())
    return df_towns.to_json()

def get_prices(department_id=None, town=None, rooms_min=1, rooms_max=10000, sq_min=1, sq_max=10000000):
    if department_id == None:
        result = france[(france["Nature mutation"] == "Vente")
                        & (france["Nombre pieces principales"].between(rooms_min, rooms_max)) 
                        & (france["Surface reelle bati"].between(sq_min, sq_max))]
        res = pd.DataFrame(result["Valeur fonciere"])
        return res.to_json()
    elif town == None:
        result = france[(france["Code departement"] == department_id)
                        & (france["Nature mutation"] == "Vente") 
                        & (france["Nombre pieces principales"].between(rooms_min, rooms_max)) 
                        & (france["Surface reelle bati"].between(sq_min, sq_max))]
        res = pd.DataFrame(result["Valeur fonciere"])
        return res.to_json()
    else:
        result = france[(france["Code departement"] == department_id) 
                        & (france["Commune"] == town) 
                        & (france["Nature mutation"] == "Vente") 
                        & (france["Nombre pieces principales"].between(rooms_min, rooms_max)) 
                        & (france["Surface reelle bati"].between(sq_min, sq_max))]
        res = pd.DataFrame(result["Valeur fonciere"])
        return res.to_json()

def get_pric():
    res = pd.DataFrame(france[france["Valeur fonciere"] > 0])
    re = res["Valeur fonciere"].to_json()
    parsed = json.loads(re)
    return json.dumps(parsed)

def get_towns_by_dep(department_id):
    result = france[france["Code departement"] == int(department_id)]                    
    res = pd.DataFrame(result["Commune"].unique())
    return res.to_json()

app = Flask(__name__)

@app.route("/")
def hello_api():
    return "<p>API</p>"

@app.route("/departments")
def departments():
    return get_departments()

@app.route("/towns")
def towns():
    return get_towns()
@app.route("/towns/<dep>")
def townsbydep(dep):
    return get_towns_by_dep(dep)

@app.route("/prices/departments/<dep_id>")
def dep(dep_id):
    return get_prices(int(dep_id))
@app.route("/prices/departments")
def dept():    
    return get_pric()


@app.route("/prices/departments/<department_id>/towns/<town_id>")
def priced(department_id, town_id):
    if request.args.get('room_min') is not None and request.args.get('room_max') is not None and request.args.get('sq_min') is not None and request.args.get('sq_max') is not None:
        r_min = request.args.get('room_min')
        r_max = request.args.get('room_max')
        s_min = request.args.get('sq_min')
        s_max = request.args.get('sq_max') 
        return get_prices(int(department_id), town_id, int(r_min), int(r_max), int(s_min), int(s_max))
    if request.args.get('room_min') is not None and request.args.get('room_max') is not None and request.args.get('sq_min') is not None:
        r_min = request.args.get('room_min')
        r_max = request.args.get('room_max')
        s_min = request.args.get('sq_min')
        return get_prices(int(department_id), town_id, int(r_min), int(r_max), int(s_min))
    if request.args.get('room_min') is not None and request.args.get('room_max') is not None:
        r_min = request.args.get('room_min')
        r_max = request.args.get('room_max')
        return get_prices(int(department_id), town_id, int(r_min), int(r_max))
    if request.args.get('room_min') is not None:
        r_min = request.args.get('room_min')
        return get_prices(int(department_id), town_id, int(r_min))
    if town_id is not None:
        return get_prices(int(department_id), town_id)
   
app.run
