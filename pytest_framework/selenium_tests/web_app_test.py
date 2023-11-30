from selenium import webdriver

driver = None


def setup_module():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("https://sdetportal.blogspot.com//")


def teardown_module():
    driver.quit()


def test_google_title():
    assert driver.title == "SDET-QA Portal"


def test_google_url():
    assert driver.current_url == "https://sdetportal.blogspot.com/"