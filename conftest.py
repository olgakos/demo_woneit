import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config #для локального запуска
from dotenv import load_dotenv
from selene.support.shared import browser


from utils import attach

DEFAULT_BROWSER_VERSION = "100.0"


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

#фикстура удаленного запуска:
@pytest.fixture(scope='function')
def setup_browser(request):
    browser.config.window_width = 1280  # NB!
    browser.config.window_height = 1400
    #browser.config.base_url = 'https://wone-it.ru'
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()
    # это capabilites Selenoid! 1_9:
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True  # !
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub", #see params here
        #command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub", #see file .env
        options=options
    )
    browser = Browser(Config(driver)) #это ЛОКАЛЬНЫЙ запуск драйвера Хром
    #browser.config.driver = driver #это УДАЛЕННЫЙ запуск драйвера Хром

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()