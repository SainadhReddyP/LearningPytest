from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="specify the browser (chrome or edge)")

@pytest.fixture(scope='class')
def launch_browser(request):
    browser_name = request.config.getoption("--browser")

    if browser_name == 'edge':
        edge_service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=edge_service)
    elif browser_name == 'chrome':
        chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=chrome_service)
    else:
        raise ValueError(f"Invalid browser specified: {request.param}")

    request.cls.driver = driver
    driver.maximize_window()
    driver.implicitly_wait(15)
    yield
    driver.quit()
