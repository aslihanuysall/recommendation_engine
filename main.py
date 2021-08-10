from EngineApi import RecoApi
from Recommendation import Recommendation

if __name__ == "__main__":
    #rec = Recommendation()
    #rec.get_item_collaborative_filtering_reco()
    #rec.get_recently_purchased_together_reco()
    #rec.get_most_purchased_in_category()
    #rec.get_most_purchased_in_subcategory()
    #All recommendation strategies have been already applied,
    #if you only want to run again, please uncomment above lines.
    reco_api = RecoApi()
    reco_api.run()
