from hypothesis import given
import hypothesis.strategies as strategies

from quicksort import quicksort


@given(strategies.lists(strategies.integers(min_value=1), min_size=1))
def test_list_size(u_list):
    original_len = len(u_list)
    quicksort(u_list)
    assert len(u_list) == original_len


@given(strategies.lists(strategies.integers(min_value=1), min_size=1))
def test_elements_in_order(u_list):
    quicksort(u_list)
    for x in range(len(u_list) - 1):
        assert u_list[x] <= u_list[x + 1]
