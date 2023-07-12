import pytest

from utils import arrs


@pytest.mark.parametrize('array, index, defaul, value', [
    ([1, 2, 3], 1, "test", 2),
    ([], 0, "test", "test"),
    ([1, 2, 3], -1, "test", "test")
])
def test_get(array, index, defaul, value):
    assert arrs.get(array, index, defaul) == value


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice([1, 2, 3], -1) == [3]
    assert arrs.my_slice([1, 2, 3], -4) == [1, 2, 3]
