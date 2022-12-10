from voluptuous import Schema, ALLOW_EXTRA

get_user_login_schema = Schema(
    {
        "data": {
            "code": int,
            "type": str,
            "message": str
        }
    },
    extra=ALLOW_EXTRA
)

get_store_order_schema = Schema(
    {
        "data": {
            "id": int,
            "petId": int,
            "quantity": int,
            "shipDate": str,
            "status": str,
            "complete": bool
        }
    },
    extra=ALLOW_EXTRA
)

post_store_order_schema = Schema(
    {
        "data": {
            "id": int,
            "petId": int,
            "quantity": int,
            "shipDate": str,
            "status": str,
            "complete": bool
        }
    },
    extra=ALLOW_EXTRA
)

delete_store_order_schema = Schema(
    {
        "data": {
            "code": int,
            "type": str,
            "message": str
        }
    },
    extra=ALLOW_EXTRA
)

post_user_createWithArray_schema = Schema(
    {
        "data": {
            "code": int,
            "type": str,
            "message": str
        }
    },
    extra=ALLOW_EXTRA
)

post_pet_create_new_schema = Schema(
    {
        "data": {
            "id": int,
  "category": {
    "id": int,
    "name": str
  },
  "name": str,
  "photoUrls": [
    str
  ],
  "tags": [
    {
      "id": int,
      "name": str
    }
  ],
  "status": str
        }
    },
    extra=ALLOW_EXTRA
)

delete_pet_schema = Schema(
    {
        "data": {
            "code": int,
            "type": str,
            "message": str
        }
    },
    extra=ALLOW_EXTRA
)