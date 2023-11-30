import pytest
from selenium import webdriver
import pytest

driver = None


@pytest.fixture(scope='module')
def init_driver():
    global driver
    driver = webdriver.Chrome()
    print("Launched the browser successfully.")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("https://sdetportal.blogspot.com//")
    yield
    print("Closed the browser successfully.")
    driver.quit()


def test_google_title(init_driver):
    print(driver.title)
    assert driver.title == "SDET Portal"


@pytest.mark.usefixtures("init_driver")
def test_google_url():
    assert driver.current_url == "https://sdetportal.blogspot.com//"