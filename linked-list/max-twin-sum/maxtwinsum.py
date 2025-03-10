class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def pair_sum(head: ListNode) -> int:
    fast, slow, stack, max_twin_sum = head, head, [], 0

    while fast and fast.next:
        fast = fast.next.next
        stack.append(slow)
        slow = slow.next

    while slow:
        max_twin_sum = max(max_twin_sum, stack.pop().val + slow.val)
        slow = slow.next

    return max_twin_sum
