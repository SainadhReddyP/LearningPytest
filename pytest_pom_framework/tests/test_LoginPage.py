from pages.LoginPage import LoginPage
from tests.test_base import BaseTest
from config.config import TestConfig
import pytest


class TestLogin(BaseTest):

    def test_selenium_practice_menu_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_selenium_practice_link()
        assert flag

    def test_login_page_title(self):
        # self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_login_page_title(TestConfig.login_page_title)
        assert title == TestConfig.login_page_title

    def test_login(self):
        # self.loginPage = LoginPage(self.driver)
        self.loginPage.login(TestConfig.username, TestConfig.password)
