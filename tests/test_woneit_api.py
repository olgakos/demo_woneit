import requests
from pytest_voluptuous import S
#from schemas import schemas
from utils.base_session import reqres_session

def test_get_good_requiest():
    response = reqres_session().get(url='/company/')
    assert response.status_code == 200
    '''
    assert response.json()["data"]
    assert response.json()["data"]["id"] == 2
    assert response.json()["data"]["email"] == "janet.weaver@reqres.in"
    assert response.json()["data"]["first_name"] == "Janet"
    assert response.json()["data"]["last_name"] == "Weaver"
    assert response.json() == S(schemas.get_single_user_schema)
    '''

def test_get_bad_request():
    response = reqres_session().get(url='/1217/')
    assert response.status_code == 404