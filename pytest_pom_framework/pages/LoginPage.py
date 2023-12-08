from config.config import TestConfig
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    """By locators"""
    username_id = (By.ID, "username")
    password_id = (By.ID, "password")
    login_btn = (By.XPATH, "//input[@value='Login']")
    selenium_practice = (By.XPATH, "//a[contains(@href,'selenium-practice')]")

    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestConfig.base_url)

    """Page Actions for Login"""

    def get_login_page_title(self, title):
        """
        description: this is used to get the page title
        :param title:
        :return:
        """
        return self.get_title(title)

    def is_selenium_practice_link(self):
        """
        description: this is used to verify selenium practice menu link
        :return:
        """
        return self.is_visible(self.selenium_practice)

    def login(self, username, password):
        """
        description: this is used to log into the application
        :param username:
        :param password:
        :return:
        """
        self.send_text(self.username_id, username)
        self.send_text(self.password_id, password)
        self.click_element(self.login_btn)
