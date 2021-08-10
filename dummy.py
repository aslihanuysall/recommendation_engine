import json
import pandas as pd

meta_df = pd.DataFrame.from_records(json.load(open("data/meta.json"))["meta"])

product_categories_df = meta_df.groupby("category")["productid"].apply(list)
product_subcategories_df = meta_df.groupby("subcategory")["productid"].apply(list)

product_subcategoraies_dict = product_subcategories_df.to_dict()
product_categories_dict = product_categories_df.to_dict()

with open("data/product_categories.json", "w") as file:
    json.dump(product_categories_dict, file,ensure_ascii=False)

with open("data/product_subcategories.json", "w") as file:
    json.dump(product_subcategoraies_dict, file,ensure_ascii=False)

product_info_dict = {d['productid']: {"name": d['name'],
                                      "category": d['category'],
                                      "subcategory": d["subcategory"]
                                      } for d in meta_df.to_dict(orient='records')}

with open("data/product_info.json", "w") as file:
    json.dump(product_info_dict, file,ensure_ascii=False)