from oddeven import ListNode, sort


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
    head = array_to_list([1, 2, 3, 4, 5])
    result = sort(head)
    assert list_to_array(result) == [1, 3, 5, 2, 4]


def test_example_2():
    head = array_to_list([2, 1, 3, 5, 6, 4, 7])
    result = sort(head)
    assert list_to_array(result) == [2, 3, 6, 7, 1, 5, 4]


def test_example_3():
    head = array_to_list([1, 2, 3, 4])
    result = sort(head)
    assert list_to_array(result) == [1, 3, 2, 4]


def test_example_4():
    head = array_to_list([1])
    result = sort(head)
    assert list_to_array(result) == [1]


def test_example_5():
    head = array_to_list([])
    result = sort(head)
    assert list_to_array(result) == []
