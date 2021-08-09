from EngineApi import RecoApi
from Recommendation import Recommendation
from EngineApi import RecoApi

if __name__ == "__main__":
    rec = Recommendation()
    rec.get_item_collaborative_filter_reco()
    rec.get_recently_purchased_together_reco()
    rec.get_most_bought_in_category()
    rec.get_most_bought_in_subcategory()
    #reco_api = RecoApi()
    #reco_api.run()