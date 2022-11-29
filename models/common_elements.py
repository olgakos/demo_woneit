from selene.support.shared import browser

def wait_short():
    browser.wait_until(300)


def go_to_page(inner_page_name):
    return browser.open(inner_page_name)