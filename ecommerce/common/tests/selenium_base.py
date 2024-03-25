import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def chrome_browser_instance(request):
    """
    This fixture returns a Chrome browser instance that is headless.
    :param request:
    :return:
    """
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(options=options)
    yield browser  # provide the fixture value
    browser.close()  # teardown
    # request.addfinalizer(lambda: browser.quit()) # teardown
    # return browser # provide the fixture value
