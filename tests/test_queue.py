import pytest
from data.queue import Queue

def test_queue_flow():
    queue = Queue()
    
    # let's insert all the items into the queue
    queue.add(item=1)
    queue.add(item=2)
    queue.add(item=3)

    actual_result = queue.queue

    assert actual_result == [1, 2, 3]

    # now it's time to remove two items
    queue.remove()
    queue.remove()

    actual_result = queue.queue
    assert actual_result == [3]


def test_raise_exception_when_try_to_remove_item_in_an_empty_queue():
    queue = Queue()

    with pytest.raises(ValueError) as exc:
        queue.remove()
        assert exc.value == "Nothing to remove into the queue"