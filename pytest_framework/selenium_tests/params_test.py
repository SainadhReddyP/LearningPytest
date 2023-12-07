from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class TestSDETPortal(BaseTest):

    @pytest.mark.parametrize(
        "username, password",
        [
            ("sainadhreddy", "automation100%"),
            ("sainadh@gmail.com", "sainadh123")
        ]
    )
    def test_login(self, username, password):
        """
        This method is used to login to sdet portal application
        :param username:
        :param password:
        :return:
        """
        self.driver.get("https://sdetportal.blogspot.com/p/login.html")
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)

