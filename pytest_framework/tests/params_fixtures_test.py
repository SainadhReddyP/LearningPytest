import pytest


@pytest.fixture(params=["a","b"])
def demo_fixture(request):
    print(request.param)


@pytest.mark.parametrize("a, b, final",[(2, 3, 5), (1, 4, 5), (9, 8, 17)])
def testAdd(a, b, final):
    assert a+b == final


def testEnterCredentials(demo_fixture):
    print("Entered credentials")


def testGetTitle(demo_fixture):
    print("Fetched the Title")