from pytest import mark
import pytest
from data.stack import Stack


@mark.parametrize(
    "first_in_first_out, stack_inputed, expected_result",
    [
        (True, [1, 2, 3], [1, 2, 3]),
        (False, [1, 2, 3], [3, 2, 1]),
    ]
)
def test_stack_flow_fifo_and_lifo(first_in_first_out, stack_inputed, expected_result):
    stack = Stack(fifo=first_in_first_out)
    # let's insert all the items into the stack
    for item in stack_inputed:
        stack.add(item)
    
    actual_result = []
    # now, let's remove all the items from the stack
    while not stack.is_empty():
        actual_result.append(stack.remove())
    
    assert actual_result == expected_result


@mark.parametrize(
    "first_in_first_out", [True, False]
)
def test_raise_exception_when_try_to_remove_item_in_an_empty_stack(first_in_first_out):
    stack = Stack(fifo=first_in_first_out)

    with pytest.raises(ValueError) as exc:
        stack.remove()
        assert exc.value == "Nothing to remove into the stack"