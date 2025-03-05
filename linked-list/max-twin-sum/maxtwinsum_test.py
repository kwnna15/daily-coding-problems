from maxtwinsum import ListNode, pair_sum


def list_to_array(head: ListNode) -> list:
    array = []
    while head:
        array.append(head.val)
        head = head.next
    return array


def array_to_list(array: list) -> ListNode:
    if not array:
        return None
    head = ListNode(array[0])
    current = head
    for val in array[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def test_example_1():
    head = array_to_list([5, 4, 2, 1])
    result = pair_sum(head)
    assert result == 6


def test_example_2():
    head = array_to_list([4, 2, 2, 3])
    result = pair_sum(head)
    assert result == 7


def test_example_3():
    head = array_to_list([1, 100000])
    result = pair_sum(head)
    assert result == 100001


def test_example_4():
    head = array_to_list([1, 2, 3, 4, 5, 6, 7, 8])
    result = pair_sum(head)
    assert result == 9


def test_example_5():
    head = array_to_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    result = pair_sum(head)
    assert result == 11
