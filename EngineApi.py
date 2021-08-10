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
        parser.add_argument('reco_strategy', required=True)
        parser.add_argument('productid', required=True)
        parser.add_argument('category', required=False)
        parser.add_argument('subcategory', required=False)

        args = parser.parse_args()
        reco_strategy = args["reco_strategy"]
        print("reco_strategy :{}".format(reco_strategy))
        productid = args["productid"]
        print("productid :{}".format(productid))
        category = args["category"]
        print("category :{}".format(category))
        subcategory = args["subcategory"]
        print("subcategory :{}".format(subcategory))

        valid_reco_strategies = ["item-collaborative-filtering", "recently_purchased_together",
                                 "most_purchased_in_category", "most_purchased_in_subcategory"]

        collaborative_filtering_recos_dict = json.load(open("recommendations/item-collaborative-filtering.json"))
        recently_purchased_together_recos_dict = json.load(open("recommendations/recently_purchased_together.json"))
        most_purchased_in_category_recos_dict = json.load(open("recommendations/most_purchased_in_category.json"))
        most_purchased_in_subcategory_recos_dict = json.load(open("recommendations/most_purchased_in_subcategory.json"))

        product_info_dict = json.load(open("data/product_info.json"))
        product_categories_dict = json.load(open("data/product_categories.json"))
        product_subcategories_dict = json.load(open("data/product_subcategories.json"))

        if (reco_strategy in valid_reco_strategies) and (productid in product_info_dict.keys()):
            if reco_strategy == "item-collaborative-filtering":
                if category or subcategory:
                    return {
                               'message': f"please do not pass category or subcategory when using "
                                          f"item-collaborative-filtering"
                           }, 404
                elif productid not in collaborative_filtering_recos_dict.keys():
                    return {
                               'message': f"item-collaborative-filtering could not found for item {productid}"
                           }, 404
                else:
                    return {productid: collaborative_filtering_recos_dict[productid]}, 200

            elif reco_strategy == "recently_purchased_together":

                if category or subcategory:
                    return {
                               'message': f"please do not pass category or subcategory when using "
                                          f"recently_purchased_together"
                           }, 404
                elif productid not in recently_purchased_together_recos_dict.keys():
                    return {
                               'message': f"recently_purchased_together_recos_dict could not found for item {productid}"
                           }, 404
                else:
                    return {productid: recently_purchased_together_recos_dict[productid]}, 200

            elif reco_strategy == "most_purchased_in_category":

                if category and not subcategory:
                    if category not in most_purchased_in_category_recos_dict.keys():
                        return {
                               'message': f"please pass a valid category when using "
                                          f"most_bought_in_category strategy"
                           }, 404

                    elif category:
                        return {productid: most_purchased_in_category_recos_dict[category][productid]}, 200

                else:
                    return  {

                                'message': f"please pass category or subcategory(not both of them) when using "
                                           f"most_bought_in_category strategy"
                            }, 404


            elif reco_strategy == "most_purchased_in_subcategory":

                if subcategory and not category:
                    if subcategory not in most_purchased_in_subcategory_recos_dict.keys():
                        return {
                                   'message': f"please pass a valid subcategory when using "
                                              f"most_bought_in_category strategy"
                               }, 404

                    elif subcategory:
                        return {productid: most_purchased_in_subcategory_recos_dict[subcategory][productid]}, 200

                else:
                    return  {

                                'message': f"please pass category or subcategory(not both of them) when using "
                                           f"most_bought_in_category strategy"
                            }, 404

        else:
            return {
               'message': "please pass valid reco_strategy and productid"
            }, 404


    def run(self):
        self.app.run()
