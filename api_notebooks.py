from flask import Flask, request
import mongoApiNotebooks
from bson.json_util import dumps

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home_page():
    return "API para indicação de notebooks para os determinados setores de uma empresa"

@app.route('/api',methods=['GET'])
def home_api():
    links_api = dumps(mongoApiNotebooks.collection_links_home_api.find({}))
    return links_api

@app.route('/api/notebooks',methods=['GET'])
def obter_notebooks():
    notebooks = dumps(mongoApiNotebooks.collection_notebooks.find({}))
    return notebooks

@app.route('/api/notebooks/<int:id>',methods=['GET'])
def obter_notebook(id):
    return dumps(mongoApiNotebooks.collection_notebooks.find({"id":id}))

@app.route('/api/marcas',methods=['GET'])
def marcas_notebook():
    marcas = dumps(mongoApiNotebooks.collection_marcas.find({}))
    return marcas

@app.route('/api/marcas/dell',methods=['GET'])
def obter_notebooks_por_marca_dell():
    dell = dumps(mongoApiNotebooks.collection_notebooks.find({"Marca":"Dell"}))
    return dell

@app.route('/api/marcas/lenovo',methods=['GET'])
def obter_notebooks_por_marca_lenovo():
    lenovo = dumps(mongoApiNotebooks.collection_notebooks.find({"Marca":"Lenovo"}))
    return lenovo

@app.route('/api/marcas/acer',methods=['GET'])
def obter_notebooks_por_marca_acer():
    acer = dumps(mongoApiNotebooks.collection_notebooks.find({"Marca":"Acer"}))
    return acer

@app.route('/api/marcas/vaio',methods=['GET'])
def obter_notebooks_por_marca_vaio():
    vaio = dumps(mongoApiNotebooks.collection_notebooks.find({"Marca":"Vaio"}))
    return vaio

@app.route('/api/marcas/samsung',methods=['GET'])
def obter_notebooks_por_marca_samsung():
    samsung = dumps(mongoApiNotebooks.collection_notebooks.find({"Marca":"Samsung"}))
    return samsung

@app.route('/api/marcas/apple',methods=['GET'])
def obter_notebooks_por_marca_apple():
    apple = dumps(mongoApiNotebooks.collection_notebooks.find({"Marca":"Apple"}))
    return apple

@app.route('/api/setores',methods=['GET'])
def setores_empresa():
    setores = dumps(mongoApiNotebooks.collection_setores.find({}))
    return setores

@app.route('/api/setores/ti',methods=['GET'])
def setor_ti():
    ti = dumps(mongoApiNotebooks.collection_notebooks.find({"Caracteristica":"Basico"}))
    return ti

@app.route('/api/setores/financeiro',methods=['GET'])
def setor_financeiro():
    financeiro = dumps(mongoApiNotebooks.collection_notebooks.find({"Caracteristica": "Basico"}))
    return financeiro

@app.route('/api/setores/rh',methods=['GET'])
def setor_rh():
    rh = dumps(mongoApiNotebooks.collection_notebooks.find({"Caracteristica": "Basico"}))
    return rh

@app.route('/api/setores/engenharia',methods=['GET'])
def setor_engenharia():
    engenharia = dumps(mongoApiNotebooks.collection_notebooks.find({
        "$and":[
            {"Caracteristica":"Performance"},
            {"GPU_dedicada":"True"}
        ]
    }))
    return engenharia

@app.route('/api/setores/projetos',methods=['GET'])
def setor_projetos():
    projetos = dumps(mongoApiNotebooks.collection_notebooks.find({"Caracteristica": "Intermediario"}))
    return projetos

@app.route('/api/setores/at',methods=['GET'])
def setor_at():
    at = dumps(mongoApiNotebooks.collection_notebooks.find({"Caracteristica": "Ultra_fino"}))
    return at

@app.route('/api/setores/diretoria',methods=['GET'])
def setor_diretoria():
    diretoria = dumps(mongoApiNotebooks.collection_notebooks.find({"Caracteristica": "Premium"}))
    return diretoria

@app.route('/api/setores/marketing', methods=['GET'])
def setor_marketing():
    diretoria = dumps(mongoApiNotebooks.collection_notebooks.find({
        "$or":[
            {"Caracteristica":"Intermediario"},
            {"Caracteristica": "Performance"}
        ]
    }))
    return diretoria

@app.route('/api/notebooks',methods=['POST'])
def adicionarNotebook():
    novo_notebook = request.get_json()
    mongoApiNotebooks.collection_notebooks.insert_one(novo_notebook)
    return "Ok"

@app.route('/api/notebooks/<int:id>',methods=['PUT'])
def alterarNotebook(id):
    alterar_notebook = request.get_json()
    filtro = {"id": id}
    novo_valor = alterar_notebook
    mongoApiNotebooks.collection_notebooks.update_many(filtro, {"$set": novo_valor})
    return "ok"
    
@app.route('/rota-existente')
def rota_existente():
    return 'Esta é uma rota existente'

@app.errorhandler(404)
def pagina_nao_encontrada(error):
    return send_file('potato.jpeg'), 404

app.run(port=5000, host='localhost', debug=True)
