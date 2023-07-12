import pytest

from utils import arrs


@pytest.mark.parametrize('array, index, defaul, value', [
    ([1, 2, 3], 1, "test", 2),
    ([], 0, "test", "test"),
    ([1, 2, 3], -1, "test", "test")
])
def test_get(array, index, defaul, value):
    assert arrs.get(array, index, defaul) == value


@pytest.mark.parametrize("coll, start, end, result", [([1, 2, 3, 4], 1, 3, [2, 3]),
                                                      ([1, 2, 3], 1, None, [2, 3]),
                                                      ([], 1, None, []),
                                                      ([1, 2, 3], -1, None, [3]),
                                                       ([1, 2, 3], -4, None, [1, 2, 3])])
def test_slice(coll, start, end, result):
    assert arrs.my_slice(coll, start, end) == result
