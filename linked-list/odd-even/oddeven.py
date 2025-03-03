class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sort(head: ListNode) -> ListNode:
    if not head:
        return head

    odd, even, even_head = head, head.next, head.next

    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next

    odd.next = even_head

    return head
