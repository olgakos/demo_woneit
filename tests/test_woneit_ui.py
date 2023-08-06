import allure
from allure_commons.types import Severity
from selene import have, by, command
from selene.support.conditions import be

from models.common_elements import wait_short, go_to_page
from models.page_company import *
from models.page_projects import *

@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Olga Kos')
@allure.description("Description: Contacts is actual (2023)")
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
        s(".footer-description").should(have.text("© 2023 Группа компаний WONE IT"))


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Olga Kos')
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
        #send_button.click()
        wait_short()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Olga Kos')
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
        wait_short()