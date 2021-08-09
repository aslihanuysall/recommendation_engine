import json
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta


class Recommendation:
    def __init__(self):
        self.events_df = pd.DataFrame.from_records(json.load(open("data/events.json"))["events"])
        self.meta_df = pd.DataFrame.from_records(json.load(open("data/meta.json"))["meta"])
        self.events_df = self.events_df[self.events_df["productid"].notnull()]
        self.events_df = self.events_df[self.events_df["productid"].notnull()]
        self.event_product_df = self.events_df.merge(self.meta_df, on="productid", how="left")

        self.product_categories_df = self.meta_df.groupby("category")["productid"].apply(list)
        self.product_categories_dict = self.product_categories_df.to_dict()

        with open("data/product_categories.json", "w") as file:
            json.dump(self.product_categories_dict, file)

        self.product_info_dict = {d['productid']: {"name": d['name'],
                                                   "category": d['category'],
                                                   "subcategory": d["subcategory"]
                                                   } for d in self.meta_df.to_dict(orient='records')}

        with open("data/product_info.json", "w") as file:
            json.dump(self.product_info_dict, file)

    def get_item_collaborative_filter_reco(self):
        purchased_df = pd.pivot_table(self.events_df, index='sessionid', columns='productid', values='event',
                                      aggfunc='count')
        purchased_df.reset_index(inplace=True)
        purchased_df = purchased_df.fillna(0)
        purchased_df = purchased_df.drop('sessionid', axis=1)

        purchased_together_df = purchased_df.T.dot(purchased_df)
        np.fill_diagonal(purchased_together_df.values, 0)

        cos_score_df = pd.DataFrame(cosine_similarity(purchased_together_df))
        cos_score_df.index = purchased_together_df.index
        cos_score_df.columns = np.array(purchased_together_df.index)

        # Take top five scoring recs that aren't the original product
        product_recs_dict = {}
        # for i in cos_score_df.index:
        for product in ["HBV00000GYMOJ", "HBV00000PV7NK", "HBV00000PV8KX"]:
            reco = cos_score_df[cos_score_df.index != product][product].sort_values(ascending=False)[0:10]
            product_recs_dict[reco.name] = reco.to_dict()

        with open("recommendations/item-collaborative-filtering.json", 'w') as file:
            json.dump(product_recs_dict, file)

    def get_recently_purchased_together_reco(self):
        product_recs_dict = {}

        self.events_df["eventtime"] = self.events_df["eventtime"].apply(
            lambda x: dt.strptime(x[:-5], "%Y-%m-%dT%H:%M:%S"))
        one_month_ago = max(self.events_df["eventtime"]) - relativedelta(months=1)
        last_one_month_events_df = self.events_df[self.events_df["eventtime"] >= one_month_ago]

        purchased_df = pd.pivot_table(last_one_month_events_df, index='sessionid', columns='productid', values='event',
                                      aggfunc='count')
        purchased_df.reset_index(inplace=True)
        purchased_df = purchased_df.fillna(0)
        purchased_df = purchased_df.drop('sessionid', axis=1)

        purchased_together_df = purchased_df.T.dot(purchased_df)
        np.fill_diagonal(purchased_together_df.values, 0)

        for product in ["HBV00000GYMOJ", "HBV00000PV7NK", "HBV00000PV8KX"]:
            reco = purchased_together_df[purchased_together_df.index != product][product].sort_values(
                ascending=False)
            product_recs_dict[reco.name] = reco.to_dict()

        with open("recommendations/recently_purchased_together.json", 'w') as file:
            json.dump(product_recs_dict, file)

    def get_most_bought_in_category(self):
        category_product_recs_dict = {}
        for category in self.product_categories_dict.keys():
            category_product_recs_dict[category] = {}
            category_sales_df = self.event_product_df[self.event_product_df["category"] == category]
            purchased_df = pd.pivot_table(category_sales_df, index='sessionid', columns='productid', values='event',
                                          aggfunc='count')
            purchased_df.reset_index(inplace=True)
            purchased_df = purchased_df.fillna(0)
            purchased_df = purchased_df.drop('sessionid', axis=1)

            purchased_together_df = purchased_df.T.dot(purchased_df)
            np.fill_diagonal(purchased_together_df.values, 0)

            product_rec_dict = {}
            for product in ["HBV00000GYMOJ", "HBV00000PV7NK", "HBV00000PV8KX"]:
                reco = purchased_df[purchased_df.index != product][product].sort_values(ascending=False)[0:10]
                product_rec_dict[reco.name] = reco.to_dict()

            category_product_recs_dict[category] = product_rec_dict[reco.name]

        with open("recommendations/most_bought_in_category.json", 'w') as file:
            json.dump(category_product_recs_dict, file)

    def get_most_bought_in_subcategory(self):
        subcategory_product_recs_dict = {}
        for subcategory in self.product_categories_dict.keys():
            subcategory_product_recs_dict[subcategory] = {}
            subcategory_sales_df = self.event_product_df[self.event_product_df["subcategory"] == subcategory]
            purchased_df = pd.pivot_table(subcategory_sales_df, index='sessionid', columns='productid', values='event',
                                          aggfunc='count')
            purchased_df.reset_index(inplace=True)
            purchased_df = purchased_df.fillna(0)
            purchased_df = purchased_df.drop('sessionid', axis=1)

            purchased_together_df = purchased_df.T.dot(purchased_df)
            np.fill_diagonal(purchased_together_df.values, 0)

            product_rec_dict = {}
            for product in ["HBV00000GYMOJ", "HBV00000PV7NK", "HBV00000PV8KX"]:
                reco = purchased_df[purchased_df.index != product][product].sort_values(ascending=False)[0:10]
                product_rec_dict[reco.name] = reco.to_dict()

            subcategory_product_recs_dict[subcategory] = product_rec_dict[reco.name]

        with open("recommendations/most_bought_in_subcategory.json", 'w') as file:
            json.dump(subcategory_product_recs_dict, file)
