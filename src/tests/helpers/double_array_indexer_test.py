import pytest
from src.helpers.double_array_indexer import double_array_indexer

two_d_array = [[1, 2], [3, 4], [5, 6]]


def test_single_array_index():
    index = [1, 1]
    assert double_array_indexer(two_d_array, index) == 4


def test_string_index():
    index = '01'
    assert double_array_indexer(two_d_array, index) == 2
