from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

"""This calss is the parent of all pages
It contains all the generic methods and utilities for all the pages"""

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def click_element(self, by_locator):
        self.wait.until(EC.visibility_of_element_located(by_locator)).click()

    def send_text(self, by_locator, text):
        self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_text(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        self.wait.until(EC.title_is(title))
        return self.driver.title

