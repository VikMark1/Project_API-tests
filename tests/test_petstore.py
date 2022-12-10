import allure
from allure_commons.types import Severity
from pytest_voluptuous import S
from schemas.petstore import get_user_login_schema, get_store_order_schema, post_store_order_schema, \
    delete_store_order_schema, post_user_createWithArray_schema, post_pet_create_new_schema, delete_pet_schema
from utils.helpers import data_login, data_create_store_order, data_create_user_withArray, \
    data_add_pet, data_update_pet

@allure.tag("API")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "VikaMark")
@allure.feature("Users - operations about user")
@allure.story("User is logged into the system")
@allure.link("https://petstore.swagger.io", name="Testing")
def test_user_login(petstore_session):
    result = petstore_session.get('/v2/user/login', json=data_login())

    with allure.step('status code is 200'):
        assert result.status_code == 200
    with allure.step('user login schema is correct'):
        assert result.json() == S(get_user_login_schema)

@allure.tag("API")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "VikaMark")
@allure.feature("Users - operations about user")
@allure.story("List of users with given input array is created")
@allure.link("https://petstore.swagger.io", name="Testing")
def test_user_createWithArray(petstore_session):
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    result = petstore_session.post(f'/v2/user/createWithArray', headers=headers, json=data_create_user_withArray())

    with allure.step('status code is 200'):
        assert result.status_code == 200
    with allure.step('message is correct'):
        assert result.json()['message'] == 'ok'
    with allure.step('user login schema is correct'):
        assert result.json() == S(post_user_createWithArray_schema)

@allure.tag("API")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "VikaMark")
@allure.feature("Store - access to Petstore orders")
@allure.story("Order for a pet is placed")
@allure.link("https://petstore.swagger.io", name="Testing")
def test_post_store_order(petstore_session):
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    result = petstore_session.post('/v2/store/order', headers=headers, json=data_create_store_order())

    with allure.step('status code is 200'):
        assert result.status_code == 200
    with allure.step('order Id is correct'):
        assert int(result.json()['id']) == 33
    with allure.step('pet Id is correct'):
        assert int(result.json()['petId']) == 335
    with allure.step('order status is correct'):
        assert result.json()['status'] == 'placed'
    with allure.step('user login schema is correct'):
        assert result.json() == S(post_store_order_schema)

@allure.tag("API")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "VikaMark")
@allure.feature("Store - access to Petstore orders")
@allure.story("Purchase order is found by ID")
@allure.link("https://petstore.swagger.io", name="Testing")
def test_get_store_order(petstore_session):
    headers = {'accept': 'application/json'}
    orderId = 33
    result = petstore_session.get(f'/v2/store/order/{orderId}', headers=headers)

    with allure.step('status code is 200'):
        assert result.status_code == 200
    with allure.step('order Id is correct'):
        assert int(result.json()['id']) == 33
    with allure.step('order status is correct'):
        assert result.json()['status'] == 'placed'
    with allure.step('user login schema is correct'):
        assert result.json() == S(get_store_order_schema)

@allure.tag("API")
@allure.severity(Severity.MINOR)
@allure.label("owner", "VikaMark")
@allure.feature("Store - access to Petstore orders")
@allure.story("Purchase order is deleted by ID")
@allure.link("https://petstore.swagger.io", name="Testing")
def test_delete_store_order(petstore_session):
    headers = {'accept': 'application/json'}
    orderId = 33
    result = petstore_session.delete(f'/v2/store/order/{orderId}', headers=headers)

    with allure.step('status code is 200'):
        assert result.status_code == 200
    with allure.step('message is correct'):
        assert isinstance(result.json()['message'], str)
    with allure.step('user login schema is correct'):
        assert result.json() == S(delete_store_order_schema)

@allure.tag("API")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "VikaMark")
@allure.feature("Pet - eveything about your Pets")
@allure.story("New pet is added to the store")
@allure.link("https://petstore.swagger.io", name="Testing")
def test_add_pet(petstore_session):
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    result = petstore_session.post('/v2/pet', headers=headers, json=data_add_pet())

    with allure.step('status code is 200'):
        assert result.status_code == 200
    with allure.step('order Id is correct'):
        assert int(result.json()['id']) == 789
    with allure.step('order status is correct'):
        assert result.json()['status'] == 'available'
    with allure.step('user login schema is correct'):
        assert result.json() == S(post_pet_create_new_schema)

@allure.tag("API")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "VikaMark")
@allure.feature("Pet - eveything about your Pets")
@allure.story("Existing pet is updated")
@allure.link("https://petstore.swagger.io", name="Testing")
def test_update_pet(petstore_session):
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    result = petstore_session.post('/v2/pet', headers=headers, json=data_update_pet())

    with allure.step('status code is 200'):
        assert result.status_code == 200
    with allure.step('order Id is correct'):
        assert int(result.json()['id']) == 789
    with allure.step('order status is correct'):
        assert result.json()['name'] == 'rocky'
    with allure.step('user login schema is correct'):
        assert result.json() == S(post_pet_create_new_schema)

@allure.tag("API")
@allure.severity(Severity.MINOR)
@allure.label("owner", "VikaMark")
@allure.feature("Pet - eveything about your Pets")
@allure.story("Pet is deleted from the store")
@allure.link("https://petstore.swagger.io", name="Testing")
def test_delete_pet(petstore_session):
    headers = {'accept': 'application/json'}
    petId = 789
    result = petstore_session.delete(f'/v2/pet/{petId}', headers=headers)

    with allure.step('status code is 200'):
        assert result.status_code == 200
    with allure.step('message is correct'):
        assert isinstance(result.json()['message'], str)
    with allure.step('user login schema is correct'):
        assert result.json() == S(delete_pet_schema)