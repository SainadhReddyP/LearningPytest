import pytest


@pytest.mark.sanity
def testLogin():
    print("Login successful")


@pytest.mark.skip
def testEnterCredentials():
    print("Entered credentials")


@pytest.mark.xfail
def testGetTitle():
    print("Fetched the Title")