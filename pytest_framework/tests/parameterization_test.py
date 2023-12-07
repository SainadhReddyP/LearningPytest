import pytest


@pytest.mark.parametrize("num, result", [(1, 11), (2, 22)])
def test_multiples_of_11(num, result):
    assert 11*num == result

