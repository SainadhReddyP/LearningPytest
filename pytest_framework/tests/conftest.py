import pytest


@pytest.fixture(autouse=True)
def reportgen():
    print("Test Reports are generated")


@pytest.fixture(scope="session", autouse=True)
def setup(browser):
    if browser == "chrome":
        print("Launch chrome")
    elif browser == "firefox":
        print("Launch firefox")
    else:
        print("Launch browser")

    print("Login")
    print("Browse products")
    yield
    print("Logoff")
    print("Close Browser")


@pytest.fixture(autouse=True, scope="session")
def environment():
    print("Launches the QA Environment")
    yield
    print("Quits the QA Environment")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption("--browser")