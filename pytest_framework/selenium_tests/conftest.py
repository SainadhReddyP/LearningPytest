import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FireFoxService

@pytest.fixture(params=["chrome","firefox"],scope="class")
def init_driver(request):
    if request.param == "chrome":
        chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
        web_driver = webdriver.Chrome(service=chrome_service)
    if request.param == "firefox":
        firefox_service = FireFoxService(executable_path=GeckoDriverManager().install())
        web_driver = webdriver.Firefox(service=firefox_service)
    request.cls.driver = web_driver
    web_driver.maximize_window()
    web_driver.implicitly_wait(10)
    yield
    web_driver.close()