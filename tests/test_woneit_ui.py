import allure
import pytest
from allure_commons.types import Severity

from selene import have, by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from models.common_elements import wait_short, go_to_page
from models.page_company import *
from models.page_projects import *

#@pytest.fixture(scope="session") #.env
@pytest.fixture(scope='function')
def setup_browser():
    browser.config.timeout = 3
    browser.config.browser_name = 'chrome'
    browser.config.base_url = 'https://wone-it.ru' #?
    browser.config.window_width = 1280
    browser.config.window_height = 1024
    yield

@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("olgakos")
@allure.description("Description: Contacts is actual (2022)")
@allure.feature("Feature: Allure with decorating")
@allure.story("Decorator")
@allure.link("https://wone-it.ru")
def test_find_basic_contacts2022(setup_browser):
    with allure.step("Open Company Page"):
        go_to_page("/company/index.php")
    with allure.step("Check actual contacts"):
        from selene.support.conditions import have
        s(".footer-phone").should(have.text("+7(499)322-05-45"))
        s(".footer-mail").should(have.text("info.ru@wone-it.ru"))
    with allure.step("Check actual year"):
        s(".footer-description").should(have.text("© 2022 Группа компаний WONE IT"))


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("olgakos")
@allure.description("Description: Fill form")
@allure.feature("Feature: Allure with decorating")
@allure.story("Decorator")
@allure.link("https://wone-it.ru")
def test_fill_form(setup_browser):
    with allure.step("Open Page"):
        go_to_page("/company/#feedback-form-wrapper")
    with allure.step("Fill form"):
        fill_contact_form()
    with allure.step("Принять политику конфиденциальности"):
        checkbox_politics.click()
    with allure.step("Submit"):
        #send_button.click() #ПРОПУСК!
        wait_short() #Временно. для удобства визуального контроля


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("olgakos")
@allure.description("Description: Search in menu")
@allure.feature("Feature: Allure with decorating")
@allure.story("Decorator")
@allure.link("https://wone-it.ru")
def test_find_some_project(setup_browser):
    with allure.step("Open Projects Page"):
        go_to_page("/projects/")
    with allure.step("Menu"):
        s(by.text("Продукты")).click()
        s(by.text("Microsoft 365")).click()
    with allure.step("Submit"):
        apply_filters.perform(command.js.scroll_into_view).click()
    with allure.step("Check"):
        s(by.partial_text("AquaHelp")).should(be.visible)
        s('#bx_3218110189_2070').should(have.text('снижает нагрузку на сотрудников'))
        wait_short() #Временно. для удобства визуального контроля