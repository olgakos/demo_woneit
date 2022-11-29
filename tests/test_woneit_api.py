import requests
from pytest_voluptuous import S
#from schemas import schemas
from utils.base_session import reqres_session

def test_get_good_requiest():
    response = reqres_session().get(url='/company/')
    assert response.status_code == 200

def test_get_bad_request():
    response = reqres_session().get(url='/1217/')
    assert response.status_code == 404

'''
import allure
from allure_commons.types import Severity

from utils.base_session import reqres_session


@allure.tag("api")
@allure.severity(Severity.NORMAL)
@allure.label("olgakos")
@allure.description("Description: Status code is 200")
@allure.feature("Feature: Allure with decorating")
@allure.story("Decorator")
@allure.link("https://wone-it.ru")
def test_get_good_requiest():
    with allure.step("Open page"):
        response = reqres_session().get(url='/company/')
    with allure.step("Verify the expected response"):
        assert response.status_code == 200


@allure.tag("api")
@allure.severity(Severity.NORMAL)
@allure.label("olgakos")
@allure.description("Description: Status code is 404")
@allure.feature("Feature: Allure with decorating")
@allure.story("Decorator")
@allure.link("https://wone-it.ru")
def test_get_bad_request():
    with allure.step("Open page"):
        response = reqres_session().get(url='/1217/')
    with allure.step("Verify the expected response"):
        assert response.status_code == 404
'''