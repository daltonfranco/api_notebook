from flask import Flask, jsonify
import requests

app = Flask(__name__)

setores = [
    {
        "ti": "http://localhost:5000/api/setores/ti",
        "Financeiro": "http://localhost:5000/api/setores/financeiro",
        "Recursos Humanos": "http://localhost:5000/api/setores/rh",
        "Engenharia": "http://localhost:5000/api/setores/engenharia",
        "Projetos": "http://localhost:5000/api/setores/projetos",
        "Assistencia Técnica": "http://localhost:5000/api/setores/at",
        "Diretoria": "http://localhost:5000/api/setores/diretoria",
        "Marketing": "http://localhost:5000/api/setores/marketing"
    }
]

marcas = [
    {
        'Dell': 'http://localhost:5000/api/marcas/dell',
        'Lenovo': 'http://localhost:5000/api/marcas/lenovo',
        'Acer': 'http://localhost:5000/api/marcas/acer',
        'Vaio': 'http://localhost:5000/api/marcas/vaio',
        'Samsung': 'http://localhost:5000/api/marcas/samsung'
    }
]

links_home_api = [
    {
        'notebook': 'http://localhost:5000/api/notebooks',
        'marcas': 'http://localhost:5000/api/marcas',
        'setores': 'http://localhost:5000/api/setores'
    }
]

notebooks = [
    {
        "id": 1,
        "Marca": "Dell",
        "Modelo": "Inspirion 13 5000",
        "url_imagem": "dell.to/3ss9lYv",
        "Valor": 6.799,
        "Caracteristica": "Ultra_fino",
        "GPU_dedicada": False,
        "Manutencao": "Media"
    },
    {
        "id": 2,
        "Marca": "Dell",
        "Modelo": "Latitude 14 3420",
        "url_imagem": "dell.to/3PomuLf",
        "Valor": 4.498,
        "Caracteristica": "Basico",
        "GPU_dedicada": False,
        "Manutencao": "Facil"
    },
    {
        "id": 3,
        "Marca": "Dell",
        "Modelo": "Vostro 3520",
        "url_imagem": "dell.to/3qPIG7o",
        "Valor": 5.699,
        "Caracteristica": "Intermediario",
        "GPU_dedicada": True,
        "Manutencao": "Facil"

    },
    {
        "id": 4,
        "Marca": "Lenovo",
        "Modelo": "IdeaPad Gaming 3i",
        "url_imagem": "lnv.gy/3OW8wOS",
        "Valor": 5.069,
        "Caracteristica": "Basico",
        "GPU_dedicada": True,
        "Manutencao": "Facil"
    },
    {
        "id": 5,
        "Marca": "Acer",
        "Modelo": "Swift SF3-314-511-56SW",
        "url_imagem": "bit.ly/44snhPh",
        "Valor": 7.399,
        "Caracteristica": "Ultra-fino",
        "GPU_dedicada": False,
        "Manutencao": "Dificil"
    },
    {
        "id": 6,
        "Marca": "Vaio",
        "Modelo": "FE15",
        "url_imagem": "bit.ly/3qGiJHr",
        "Valor": 4.223,
        "Caracteristica": "Basico",
        "GPU_dedicada": False,
        "Manutencao": "Dificil"
    },
    {
        "id": 7,
        "Marca": "Samsung",
        "Modelo": "Galaxy Book 3",
        "url_imagem": "bit.ly/3KV7hyo",
        "Valor": 9.219,
        "Caracteristica": "Ultra_fino",
        "GPU_dedicada": True,
        "Manutencao": "Dificil"
    },
    {
        "id": 8,
        "Marca": "Dell",
        "Modelo": "XPS 13 Plus",
        "url_imagem": "dell.to/3QYEvks",
        "Valor": 12.899,
        "Caracteristica": "Premium",
        "GPU_dedicada": False,
        "Manutencao": "Dificil"
    },
    {
        "id": 9,
        "Marca": "Apple",
        "Modelo": "Macbook Air 13 M2",
        "url_imagem": "apple.co/45qlZFX",
        "Valor": 12.499,
        "Caracteristica": "Premium",
        "GPU_dedicada": False,
        "Manutencao": "Especialista"
    },
    {
        "id": 10,
        "Marca": "Dell",
        "Modelo": "Precision 3581",
        "url_imagem": "dell.to/3OR2E9W",
        "Valor": 25.409,
        "Caracteristica": "Performance",
        "GPU_dedicada": True,
        "Manutencao": "Media"
    },
    {
        "id": 11,
        "Marca": "Vaio",
        "Modelo": "Z",
        "url_imagem": "https://www.br.vaio.com/arquivos/infografico-z-usabilidade-2022.jpg?v=637891697599730000",
        "Valor": 19.007,
        "Caracteristica": "Ultra_fino",
        "GPU_dedicada": False,
        "Manutencao": "Dificil"
    },
    {
        "id": 12,
        "Marca": "Acer",
        "Modelo": "Predator Helios 300 PH315-54-70LH",
        "url_imagem": "https://acerstore.vtexassets.com/arquivos/ids/160629-1200-auto?v=637878021037370000&width=1200&height=auto&aspect=true",
        "Valor": 8.999,
        "Caracteristica": "Intermediario",
        "GPU_dedicada": True,
        "Manutencao": "Media"
    },
    {
        "id": 13,
        "Marca": "Lenovo",
        "Modelo": "ThinkPad X1 Carbon",
        "url_imagem": "https://www.lenovo.com/medias/?context=bWFzdGVyfHJvb3R8MTEyMjY5fGltYWdlL3BuZ3xoODQvaGY3LzExMzIwNTM4Mzk4NzUwLnBuZ3xmMGVmNTk5MWMwNTMyOGI3MTY4MTY3MjJlZjRlZmFkNmY4OTA5YTUyOGJmZmVkYzg2NzJiYzMyNzBjMzNjMWM2",
        "Valor": 11.699,
        "Caracteristica": "Intermediario",
        "GPU_dedicada": False,
        "Manutencao": "Media"
    },
    {
        "id": 14,
        "Marca": "Samsung",
        "Modelo": "Galaxy book3 ultra",
        "url_imagem": "https://images.samsung.com/is/image/samsung/assets/br/computers/samsung-book/feature/Book3-Ultra_banner-Windows-2-pc.png?$ORIGIN_PNG$",
        "Valor": 16.317,
        "Caracteristica": "Performance",
        "GPU_dedicada": True,
        "Manutencao": "Dificil"
    },
    {
        "id": 15,
        "Marca": "Dell",
        "Modelo": "Latitude 5430",
        "url_imagem": "https://i.dell.com/is/image/DellContent/content/dam/ss2/product-images/dell-client-products/notebooks/latitude-notebooks/14-5430/media-gallery/laptop-latitude-14-5430-gray-gallery-3.psd?fmt=png-alpha&pscan=auto&scl=1&hei=402&wid=566&qlt=100,1&resMode=sharp2&size=566,402&chrss=full",
        "Valor": 8.098,
        "Caracteristica": "Intermediario",
        "GPU_dedicada": False,
        "Manutencao": "Facil"
    },
    {
        "id": 16,
        "Marca": "Samsung",
        "Modelo": "Samsung book",
        "url_imagem": "https://images.samsung.com/is/image/samsung/p6pim/br/feature/164228315/br-feature-notebook-plus2-np550xdai-436300-533833977",
        "Valor": 4.399,
        "Caracteristica": "Basico",
        "GPU_dedicada": False,
        "Manutencao": "Dificil"
    },
    {
        "id": 17,
        "Marca": "Lenovo",
        "Modelo": "ThinkPad X1 Titanium Yoga",
        "url_imagem": "https://www.lenovo.com/medias/Notebook-Lenovo-X1-Titanium-Yoga-4.jpg?context=bWFzdGVyfHJvb3R8NDU5MjM5fGltYWdlL2pwZWd8aDFjL2g1Zi8xMjU4NDA3MzQ2MTc5MC5qcGd8MzcwNThjMDBhYjc4M2E5ODJiODdkODE2ZmU3NzMyMTI4ODg5MThmYWZhZDhjMzBlMjlhM2VlNDVkYjYxYTIxZg",
        "Valor": 13.500,
        "Caracteristica": "Ultra_fino",
        "GPU_dedicada": False,
        "Manutencao": "Media"
    },
    {
        "id": 18,
        "Marca": "Acer",
        "Modelo": "Aspire 5 A514-54-789C ",
        "url_imagem": "https://acerstore.vtexassets.com/arquivos/ids/160495-1200-auto?v=637873592288000000&width=1200&height=auto&aspect=true",
        "Valor": 4.299,
        "Caracteristica": "Basico",
        "GPU_dedicada": False,
        "Manutencao": "Media"
    },
    {
        "id": 19,
        "Marca": "Acer",
        "Modelo": "Acer Swift 5 SF514-56T-50WL",
        "url_imagem": "https://acerstore.vtexassets.com/arquivos/ids/160960-1200-auto?v=637937485984800000&width=1200&height=auto&aspect=true",
        "Valor": 12.999,
        "Caracteristica": "Premium",
        "GPU_dedicada": False,
        "Manutencao": "Dificil"
    },
    {
        "id": 20,
        "Marca": "Apple",
        "Modelo": "Macbook pro 14 m2 pro",
        "url_imagem": "https://www.apple.com/v/macbook-pro-14-and-16/e/images/overview/performance/choose_size__b11uc4j8f36u_large_2x.jpg",
        "Valor": 23.999,
        "Caracteristica": "Performance",
        "GPU_dedicada": False,
        "Manutencao": "Especialista"
    }
]

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
        if notebooks[engenharia]["Caracteristica"] == "Performance" and notebooks[engenharia]["GPU_dedicada"] == True:
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


app.run(port=5000, host='localhost', debug=True)