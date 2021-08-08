import json
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class Recommendation:
    def __init__(self):
        self.events_df = pd.DataFrame.from_records(json.load(open("data/events.json")))
        self.meta_df = pd.DataFrame.from_records(json.load(open("data/meta.json")))

    def get_item_item_collaborative_filter_reco(self):
        pivot_df = pd.pivot_table(self.events_df, index='sessionid', columns='productid', values='event', aggfunc='count')
        pivot_df.reset_index(inplace=True)
        pivot_df = pivot_df.fillna(0)
        pivot_df = pivot_df.drop('sessionid', axis=1)

        co_matrix = pivot_df.T.dot(pivot_df)
        np.fill_diagonal(co_matrix.values, 0)

        cos_score_df = pd.DataFrame(cosine_similarity(co_matrix))
        cos_score_df.index = co_matrix.index
        cos_score_df.columns = np.array(co_matrix.index)

        # Take top five scoring recs that aren't the original product
        product_recs_dict = {}
        #for i in cos_score_df.index:
        for i in ["HBV00000GYMOJ","HBV00000PV7NK","HBV00000PV8KX"]:
            reco = cos_score_df[cos_score_df.index!=i][i].sort_values(ascending = False)[0:10]
            product_recs_dict[reco.name] = reco.to_dict()

        with open("item-item-collaborative-filtering.json") as file:
            json.dump(product_recs_dict, file)

    #def get_last_purchased_reco(self):


    #def get_bought_together_reco(self):


    #def get_most_bought_in_category(self):

    #def get_most_bought_in_subcategory(self):