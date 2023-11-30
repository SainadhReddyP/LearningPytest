import pytest


@pytest.mark.regression
def testCalculation():
    assert 9+9 == 18