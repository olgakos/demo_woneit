import allure
from allure_commons.types import Severity

from utils.base_session import reqres_session


@allure.tag("api")
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Olga Kos')
@allure.description("Status code is 200")
@allure.feature("Opening pages")
@allure.story("Page is available")
@allure.link("https://wone-it.ru")
def test_get_good_requiest():
    with allure.step("Open page"):
        response = reqres_session().get(url='/company/')
    with allure.step("Verify the expected response"):
        assert response.status_code == 200


@allure.tag("api")
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Olga Kos')
@allure.description("Status code is 404")
@allure.feature("Opening pages")
@allure.story("Page is NOT available")
@allure.link("https://wone-it.ru")
def test_get_bad_request():
    with allure.step("Open page"):
        response = reqres_session().get(url='/1217/')
    with allure.step("Verify the expected response"):
        assert response.status_code == 404

