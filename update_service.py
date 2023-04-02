from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from pymongo import MongoClient
from mongodb_url import mongoDB_url
from helper import Database_usage

app = Flask(__name__)
api = Api(app)
client = MongoClient(mongoDB_url())
db = client["mydatabase"]
collection = db["practice"]

class Service(Resource):    
    def put(self, phone,new_price):
        try:
            service = collection.find_one({'phone': phone})
            if not service:
                return {'error': 'Service not found'}
            
            #new_price = request.json['price']
            collection.update_one({'phone':phone}, {'$set': {'price': new_price}})
            
            return {'message': 'Service price updated successfully'}
        except Exception as e:
            return {'error': str(e)}

api.add_resource(Service, '/services_update/<int:phone>/<int:new_price>')

if __name__ == '__main__':
    app.run(debug=True)
