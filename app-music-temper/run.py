# -*- coding: utf-8 -*-
"""
Spyder Editor
Este é um arquivo de script temporário.
Fonte de apoio: http://pythonclub.com.br/what-the-flask-pt-1-introducao-ao-desenvolvimento-web-com-python.html#views_e_roteamento_de_urls
                https://blog.4linux.com.br/flask-basico/
"""
#---------------------------------------------------------------------------------------------------#
import flask
from flask import Flask, jsonify, render_template, request
import requests
import json
#---------------------------------------------------------------------------------------------------#
app = Flask(__name__)

#---------------------------------------------------------------------------------------------------#

def f_estilo_musical(local):
    v_cidade = local 
    v_url_api_weather = 'http://api.openweathermap.org/data/2.5/weather?q='+v_cidade.capitalize()+'&units=metric&APPID=60d00bbb5151187c0df71b7aa55728ba'
    req = requests.get(v_url_api_weather)    
    dicionario = json.loads(req.text)
    v_temperatura  = dicionario['main']['temp']
    
    v_param_musica = ''
    if v_temperatura <= 10 :
        v_param_musica = 'Clássica'
        v_sugestao_playlist = 'classico'
    elif v_temperatura > 10  and v_temperatura < 25 :
        v_param_musica = 'Rock'
        v_sugestao_playlist = 'rock'
    elif v_temperatura >= 25 :
        v_param_musica = 'Pop'
        v_sugestao_playlist = 'pop'
    else:
        v_param_musica = 'erro'
    return [v_param_musica,v_temperatura, str.capitalize(v_cidade), v_sugestao_playlist]
    
# f_estilo_musical('guarulhos')
    
#---------------------------------------------------------------------------------------------------#
@app.route("/<local>")
def lista_de_musicas(local):
    v1 = f_estilo_musical(local)
    return render_template("lista_de_musicas.html", estilo=v1[0], temperatura=v1[1], cidade=v1[2], sugestao_playlist=v1[3]), 200

if __name__ == '__main__':
    app.run(debug=True)
