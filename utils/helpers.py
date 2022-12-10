import os
from dotenv import load_dotenv


def data_login():
    load_dotenv()
    LOGIN = os.getenv('user_login')
    PASSWORD = os.getenv('user_password')
    data = {
        "username": LOGIN,
        "password": PASSWORD
    }
    return data

def data_create_store_order():
    data = {
        "id": 33,
        "petId": 335,
        "quantity": 1,
        "shipDate": "2022-12-08T18:56:46.444Z",
        "status": "placed",
        "complete": True
    }
    return data

def data_create_user_withArray():
    data = [
        {
            "id": 7,
            "username": "testUser1",
            "firstName": "test1",
            "lastName": "user1",
            "email": "test@test.com",
            "password": "1234",
            "phone": "11111111",
            "userStatus": 0
        }
]
    return data

def data_update_user():
    data = [
        {
            "id": 7,
            "username": "testUser1",
            "firstName": "test2",
            "lastName": "user2",
            "email": "test@test.com",
            "password": "5678",
            "phone": "2222222222",
            "userStatus": 0
        }
]
    return data

def data_add_pet():
    data = {
        "id": 789,
  "category": {
    "id": 789,
    "name": "dogs"
  },
  "name": "doggie",
  "photoUrls": [
    "test"
  ],
  "tags": [
    {
      "id": 789,
      "name": "puppy"
    }
  ],
  "status": "available"
    }
    return data

def data_update_pet():
    data = {
        "id": 789,
  "category": {
    "id": 789,
    "name": "dogs"
  },
  "name": "rocky",
  "photoUrls": [
    "test2"
  ],
  "tags": [
    {
      "id": 789,
      "name": "puppy2"
    }
  ],
  "status": "available"
    }
    return data