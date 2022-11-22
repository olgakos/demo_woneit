import allure
import pytest
from selene.support import by
from selene.support.conditions import be, have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from selene import be, have, command

@pytest.fixture(scope='function')
def setup_browser():
    browser.config.timeout = 3
    browser.config.browser_name = 'chrome'
    browser.config.base_url = 'https://wone-it.ru'
    browser.config.window_width = 1280
    browser.config.window_height = 1024
    yield

def test_pass1():
    pass

def test_find_basic_contacts2022(setup_browser):
    with allure.step("Open Company Page"):
        browser.open("/company/index.php")
    with allure.step("Check actual contacts"):
        s(".footer-phone").should(have.text("+7(499)322-05-45"))
        s(".footer-mail").should(have.text("info.ru@wone-it.ru"))
    with allure.step("Check actual year"):
        s(".footer-description").should(have.text("© 2022 Группа компаний WONE IT"))

def test_some_project(setup_browser):
    with allure.step("Open Projects Page"):
        browser.open("/projects/")
    with allure.step("Menu"):
        s(by.text("Продукты")).click()
        s(by.text("Microsoft 365")).click()
    with allure.step("Submit"):
        #s("#set_filter").click()
        s('#set_filter').perform(command.js.scroll_into_view).click() #убедиться, что кнопка доступна
    with allure.step("Check"):
        s(by.partial_text("AquaHelp")).should(be.visible)
        #s('.projects-slide-item-description').should(have.text('Онлайн-библиотека переводит все офисные бизнес-процессы в Microsoft 365'))
        s('#bx_3218110189_2070').should(have.text('снижает нагрузку на сотрудников'))
        #browser.wait_until(500)

def test_fill_form(setup_browser):
    with allure.step("Open Page"):
        browser.open("/company/#feedback-form-wrapper")
    with allure.step("Fill Form"):
        s('[name="NAME"]').type('Test').press_enter()
        s('[name="SURNAME"]').type('Test').press_enter()
        s('[name="COMPANY"]').type('Test').press_enter()
        s('[name="STATUS"]').type('Test').press_enter()
        s('[name="PHONE"]').type('12345').press_enter()
        s('[name="EMAIL"]').type('Test').press_enter()
        s('[name="MESSAGE"]').type('Test').press_enter()
    with allure.step("Политикой конфиденциальности"):
        s("[for='feedback-agree']").click()
    with allure.step("Submit"):
        #s(".feedback-form__bottom").click() #ПРОПУСК!
        browser.wait_until(500)