# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import time
import requests
import pandas as pd
import os
import datetime
import decimal
import csv
import json
from pandas.io.json import json_normalize
import decimal as Decimal


################################################################################################################
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
 
from my_app.catalog.views import catalog
app.register_blueprint(catalog)
 
db.create_all()

################################################################################################################
 #verifica temperatura
v_cidade = input('Qual sua cidade?')
 
v_url_api_weather = 'http://api.openweathermap.org/data/2.5/weather?q='+v_cidade.capitalize()+'&units=metric&APPID=60d00bbb5151187c0df71b7aa55728ba'
req = requests.get(v_url_api_weather)
print(req.text)

dicionario = json.loads(req.text)
v_temperatura  = dicionario['main']['temp']

v_param_musica = ''
if v_temperatura <= 10 :
    print('Tá frio ai heim! Sugerimos Música Clássica, para relaxar e descansar debaixo do cobertor')
    v_param_musica = 'classica'
elif v_temperatura > 10  and v_temperatura < 25 :
    print('Humm...,\nTemperatura ideal para ouvir um Rock!')
    v_param_musica = 'rock'
elif v_temperatura >= 25 :
    print('Pop é a sugestão ideal para o momento!')
    v_param_musica = 'pop'
else:
    print('Ops algo deu errado, tente novamente daqui a pouco, plzzz =D')
    v_param_musica = 'erro'
