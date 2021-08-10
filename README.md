# recommendation_engine

-Before using this repository, required packages needs to be installed;
-Easiest way to install packagess into a python virtual environment;
-python -m pip install -r requirements.txt 

There are different strategies for suggesting related products:

- Item - Collaborative Filtering
- Recently - Purchased Together
- Most - Purchased Item in Same Category
- Most - Purchased Item in Same SubCategory

**How to use recommendation-engine REST-API**
----
Returns json data recommendations with scores for a single product.

* **URL**

  http://127.0.0.1:5000/recommended_products/:params

* **Method:**

  `GET`

* **URL Params**

  **Required:**

  `strategy=[string]`
  `productid=[string]`

  **Optional:**
  `category=[string]`
  `subcategorty=[string]`

* **Data Params**

  None

* **Success Responses:**

    * **Code:** 200 <br />
      **Content:** `{ productid : {recommended_products} }`

* **Error Responses:**

    * **Code:** 404 <br />
    * **Content:** `error : please pass a valid recommendation strategy and productid `

  OR

    * **Code:** 404 <br /><
      **Content:** `error : please do not pass category or subcategory when using item-collaborative-filtering`

  OR

    * **Code:** 404 <br /><
      **Content:** `error : please do not pass category or subcategory when using recently_purchased_together`

  OR
    * **Code:** 404 <br /><
      **Content:** `error : please pass category or subcategory when using most_bought_in_category strategy`

  OR
    * **Code:** 404 <br /><
      **Content:** `error : please pass category or subcategory when using most_bought_in_subcategory strategy`

## Success Response Examples

For a single valid productid with a valid strategy on the local database where that productid, all responsed return most
related products for a given product.

**Code** : `200 OK`

**Content examples**

Item Collaborating filtering example
http://127.0.0.1:5000/recommended_products?reco_strategy=item-collaborative-filtering&productid=HBV00000GYMOJ

```json
{
  "HBV00000GYMOJ": {
    "HBV00000PV7NK": 0.8929077906802638,
    "AILEBIZIZSMTLDGY54": 0.8620772965041889,
    "HBV00000PV8KX": 0.8570616428945494,
    "HBV00000PVPZ5": 0.8335853014699707,
    "HBV00000PV7NG": 0.8296161628171579,
    "HBV00000PV7NP": 0.8296161628171579,
    "HBV00000PV7NU": 0.8280374436647528,
    "HBV000009FFMQ": 0.8270889818100403,
    "HBV00000PV5VQ": 0.8254751220429825,
    "HBV00000PV8KN": 0.8192363191151126
  }
}
```

Recently Purchased Together Example
http://127.0.0.1:5000/recommended_products?reco_strategy=recently_purchased_together&productid=AILEBIZIZSMTLDGY54
```json
{
  "AILEBIZIZSMTLDGY54": {
    "HBV00000PV7O3": 9.0,
    "AILEBIZIZSMTLDHB18": 6.0,
    "AILEMTTDMT57": 6.0,
    "HBV00000QU6GQ": 6.0,
    "HBV00000PVBJY": 6.0,
    "HBV00000PV5VU": 6.0,
    "HBV00000GYMOJ": 6.0,
    "HBV00000PV8BL": 5.0,
    "OYUNMTTW2087": 5.0,
    "HBV00000NGXFE": 5.0
  }
}
```

Most Purchased In Same Category Example
http://127.0.0.1:5000/recommended_products?reco_strategy=most_purchased_in_category&productid=HBV000003GPSJ&category=Atıştırmalık
```json
{
  "HBV000003GPSJ": {
    "HBV00000JUHLM": 7.0,
    "ZYHPETICEBSK107": 5.0,
    "HBV0000054IPN": 5.0,
    "ZYHPETICEBSK080": 5.0,
    "HBV00000QU4CI": 4.0,
    "HBV00000QU4BW": 3.0,
    "HBV00000JBL0D": 3.0,
    "HBV00000PVCRI": 3.0,
    "HBV00000JUHL6": 3.0,
    "HBV00000NE1VV": 3.0
  }
}
```

Most Purchased In Same SubCategory Example
http://127.0.0.1:5000/recommended_products?reco_strategy=most_purchased_in_subcategory&productid=HBV00000PVQKS&subcategory=Alt Açma Seti
```json
{
  "HBV00000PVQKS": {
    "HBV00000PVR10": 0.0,
    "ZYCANN63125": 0.0,
    "ZYECZACI9470301": 0.0,
    "ZYHAYAT803989": 0.0
  }
}
```