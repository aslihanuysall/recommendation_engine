from flask import Flask
from flask_restful import Resource, Api, reqparse
import json
import ast
app = Flask(__name__)
api = Api(app)

class RecoApi(Resource):
    # methods go here
    def get(self):
        data = json.load(open("recommendations/item-item-collaborative-filtering.json"))
        return {'data': data}, 200  # return data and 200 OK code
    #pass

api.add_resource(RecoApi, '/recommended_products')
