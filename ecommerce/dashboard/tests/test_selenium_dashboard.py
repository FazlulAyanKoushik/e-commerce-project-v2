import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.selenium
def test_create_admin_user(create_admin_user):
    """
    Check if the user is created successfully
        :param create_admin_user:
    """
    assert create_admin_user.__str__() == "01515620300"


@pytest.mark.selenium
def test_dashboard_admin_login(live_server, chrome_browser_instance, create_admin_user):
    """
    This test checks if the admin user can log in to the admin dashboard.
    """
    browser = chrome_browser_instance
    browser.get(live_server.url + "/admin/")

    username_input = browser.find_element(By.NAME, "username")
    username_input.send_keys("01515620300")

    password_input = browser.find_element(By.NAME, "password")
    password_input.send_keys("admin")

    password_input.send_keys(Keys.RETURN)

    assert "Site administration" in browser.page_source
