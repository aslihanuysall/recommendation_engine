from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import json
import ast

class RecoApi(Resource):

    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(RecoApi, '/recommended_products')

# methods
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('productid', required=True)
        parser.add_argument('reco_strategy', required=True)
        parser.add_argument('categoryid', required=False)
        parser.add_argument('subcategoryid', required=False)

        args = parser.parse_args()
        recommendations = json.load(open("recommendations/item-item-collaborative-filtering.json"))
        #categories = json.load(open("data/product-categories.json"))

        return recommendations[args["productid"]]
        #if args['productid'] in list(recommendations.keys()):
        #    if
#
        #    return {
        #               'message': f"'{args['userId']}' already exists."
        #           }, 409
        #else:
        #    print()
        #return {'data': data}, 200  # return data and 200 OK code


    def run(self):
        self.app.run()

    #def get_last_purchased_reco(self):


    #def get_bought_together_reco(self):


    #def get_most_bought_in_category(self):

    #def get_most_bought_in_subcategory(self):
#reco_api.app.run()

