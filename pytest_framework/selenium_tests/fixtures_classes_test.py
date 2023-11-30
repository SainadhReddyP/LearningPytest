from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as GeckoService
import pytest


@pytest.fixture(scope='class')
def init_chrome_driver(request):
    chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
    chrome_driver = webdriver.Chrome(service=chrome_service)
    request.cls.driver = chrome_driver
    chrome_driver.maximize_window()
    yield
    chrome_driver.close()


@pytest.fixture(scope='class')
def init_firefox_driver(request):
    firefox_service = GeckoService(executable_path=GeckoDriverManager().install())
    ff_driver = webdriver.Firefox(service=firefox_service)
    request.cls.driver = ff_driver
    ff_driver.maximize_window()
    yield
    ff_driver.close()


@pytest.mark.usefixtures('init_chrome_driver')
class BaseChromeTest:
    pass


class TestGoogleChrome(BaseChromeTest):

    def test_sdet_title_chrome(self):
        self.driver.get("https://sdetportal.blogspot.com/")
        assert self.driver.title == "SDET-QA PORTAL"


# @pytest.mark.usefixtures('init_firefox_driver')
# class BaseFireFoxTest:
#     pass
#
#
# class TestFireFoxChrome(BaseFireFoxTest):
#
#     def test_sdet_title_ff(self):
#         self.driver.get("https://sdetportal.blogspot.com/")
#         assert self.driver.title == "SDET-QA PORTAL"
#
