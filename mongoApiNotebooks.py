import pymongo

cluster = pymongo.MongoClient('mongodb+srv://dalton:dalton@cluster0.ydgutjg.mongodb.net/')

db = cluster.get_database('api-notebooks')

collection_setores = db.get_collection('setores')
collection_notebooks = db.get_collection('notebooks')
collection_links_home_api = db.get_collection('links-home-api')
collection_marcas = db.get_collection('marcas')