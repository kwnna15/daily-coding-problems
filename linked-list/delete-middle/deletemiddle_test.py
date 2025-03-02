from deletemiddle import ListNode, delete


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
    head = array_to_list([1, 3, 4, 7, 1, 2, 6])
    result = delete(head)
    assert list_to_array(result) == [1, 3, 4, 1, 2, 6]


def test_example_2():
    head = array_to_list([1, 2, 3, 4])
    result = delete(head)
    assert list_to_array(result) == [1, 2, 4]


def test_example_3():
    head = array_to_list([2, 1])
    result = delete(head)
    assert list_to_array(result) == [2]


def test_example_4():
    head = array_to_list([1])
    result = delete(head)
    assert list_to_array(result) == []


def test_example_5():
    head = array_to_list([1, 2, 3, 4, 5])
    result = delete(head)
    assert list_to_array(result) == [1, 2, 4, 5]
