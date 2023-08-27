from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

with open('setores.json') as setor:
    setores = json.load(setor)

with open('marcas.json') as marca:
    marcas = json.load(marca)

with open('links_home_api.json') as api_home:
    links_home_api = json.load(api_home)

with open('notebooks.json') as notebook:
    notebooks = json.load(notebook)


@app.route('/api/notebooks/<int:id>',methods=['GET'])
def obter_notebook(id):
    for notebook in notebooks:
        if notebook.get('id') == id:
            return jsonify(notebook)

@app.route('/',methods=['GET'])
def home_page():
    return "API para indicação de notebooks para os determinados setores de uma empresa"

@app.route('/api/notebooks',methods=['GET'])
def obter_notebooks():
    return jsonify(notebooks)

@app.route('/api/marcas',methods=['GET'])
def marcas_notebook():
    return jsonify(marcas)

@app.route('/api',methods=['GET'])
def home_api():
    return jsonify(links_home_api)

@app.route('/api/setores',methods=['GET'])
def setores_empresa():
    return jsonify(setores)

@app.route('/api/marcas/dell',methods=['GET'])
def obter_notebooks_por_marca_dell():
    lista_dell = []
    for x in range(len(notebooks)):
        if notebooks[x]['Marca'] == 'Dell':
            lista_dell.append(notebooks[x])
    return lista_dell

@app.route('/api/marcas/lenovo',methods=['GET'])
def obter_notebooks_por_marca_lenovo():
    lista_lenovo = []
    for y in range(len(notebooks)):
        if notebooks[y]['Marca'] == 'Lenovo':
            lista_lenovo.append(notebooks[y])
    return lista_lenovo

@app.route('/api/marcas/acer',methods=['GET'])
def obter_notebooks_por_marca_acer():
    lista_acer = []
    for a in range(len(notebooks)):
        if notebooks[a]['Marca'] == 'Acer':
            lista_acer.append(notebooks[a])
    return lista_acer

@app.route('/api/marcas/vaio',methods=['GET'])
def obter_notebooks_por_marca_vaio():
    lista_vaio = []
    for v in range(len(notebooks)):
        if notebooks[v]['Marca'] == "Vaio":
            lista_vaio.append(notebooks[v])
    return lista_vaio

@app.route('/api/marcas/samsung',methods=['GET'])
def obter_notebooks_por_marca_samsung():
    lista_samsung = []
    for s in range(len(notebooks)):
        if notebooks[s]['Marca'] == "Samsung":
            lista_samsung.append(notebooks[s])
    return lista_samsung

@app.route('/api/setores/ti',methods=['GET'])
def setor_ti():
    return "T.I"

@app.route('/api/setores/financeiro',methods=['GET'])
def setor_financeiro():
    lista_financeiro = []
    for financeiro in range(len(notebooks)):
        if notebooks[financeiro]["Caracteristica"] == "Basico":
            lista_financeiro.append(notebooks[financeiro])
    return lista_financeiro

@app.route('/api/setores/rh',methods=['GET'])
def setor_rh():
    lista_rh = []
    for rh in range(len(notebooks)):
        if notebooks[rh]["Caracteristica"] == "Basico":
            lista_rh.append(notebooks[rh])
    return lista_rh

@app.route('/api/setores/engenharia',methods=['GET'])
def setor_engenharia():
    lista_engenharia = []
    for engenharia in range(len(notebooks)):
        if notebooks[engenharia]["Caracteristica"] == "Performance" and notebooks[engenharia]["GPU_dedicada"] == "True":
            lista_engenharia.append(notebooks[engenharia])
    return lista_engenharia

@app.route('/api/setores/projetos',methods=['GET'])
def setor_projetos():
    lista_projetos = []
    for projeto in range(len(notebooks)):
        if notebooks[projeto]["Caracteristica"] == "Intermediario":
            lista_projetos.append(notebooks[projeto])
    return lista_projetos

@app.route('/api/setores/at',methods=['GET'])
def setor_at():
    lista_at = []
    for at in range(len(notebooks)):
        if notebooks[at]["Caracteristica"] == "Ultra_fino":
            lista_at.append(notebooks[at])
    return lista_at

@app.route('/api/setores/diretoria',methods=['GET'])
def setor_diretoria():
    lista_diretoria = []
    for diretoria in range(len(notebooks)):
        if notebooks[diretoria]["Caracteristica"] == "Premium":
            lista_diretoria.append(notebooks[diretoria])
    return lista_diretoria

@app.route('/api/setores/marketing', methods=['GET'])
def setor_marketing():
    lista_mk = []
    for mk in range(len(notebooks)):
        if notebooks[mk]["Caracteristica"] == "Performance" or notebooks[mk]["Caracteristica"] == "Intermediario":
            lista_mk.append(notebooks[mk])
    return lista_mk

@app.route('/api/marcas/apple',methods=['GET'])
def obter_notebooks_por_marca_apple():
    lista_apple = []
    for ap in range(len(notebooks)):
        if notebooks[ap]['Marca'] == "Apple":
            lista_apple.append(notebooks[ap])
    return lista_apple


app.run(port=5000, host='localhost', debug=True)