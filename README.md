# recommendation_engine

There are different strategies for suggesting related products:

- Item - Item Collaborative Filtering
- Last - Purchased Item In Same Category
- Last - Purchased Item in Same SubCategory
- Last - Purchased Together

**How to use**
----
Returns json data recommendations for a single product.

* **URL**

  /recommended_products/:id

* **Method:**

  `GET`

*  **URL Params**

   **Required:**

   `id=[integer]`

* **Data Params**

  None

* **Success Response:**

    * **Code:** 200 <br />
      **Content:** `{ id : 12, name : "Michael Bloom" }`

* **Error Response:**

    * **Code:** 404 NOT FOUND <br />
      **Content:** `{ error : "User doesn't exist" }`

  OR

    * **Code:** 401 UNAUTHORIZED <br /><
      **Content:** `{ error : "You are unauthorized to make this request." }`

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/users/1",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
