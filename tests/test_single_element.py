import pytest

from single_element import find_single


def test_example_case():
    assert find_single([1, 2, 3, 4, 3, 1, 2]) == 4


def test_single_element_only():
    assert find_single([7]) == 7


def test_negative_numbers():
    assert find_single([-1, 2, 2, 3, 3]) == -1


def test_zero_as_single_element():
    assert find_single([0, 5, 5, 8, 8]) == 0


def test_larger_array():
    assert find_single([10, 4, 6, 4, 10, 9, 6]) == 9


def test_empty_array_raises_error():
    with pytest.raises(ValueError):
        find_single([])


def test_even_length_array_raises_error():
    with pytest.raises(ValueError):
        find_single([1, 1, 2, 2])

def test_required_libraries_are_installed():
    import numpy
    import pandas
    import matplotlib
    import seaborn

    assert numpy is not None
    assert pandas is not None
    assert matplotlib is not None
    assert seaborn is not None