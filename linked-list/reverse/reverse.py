class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse(head: ListNode) -> ListNode:
    curr = head
    prev = None

    while curr != None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev
