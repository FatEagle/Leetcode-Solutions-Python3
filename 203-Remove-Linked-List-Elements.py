# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Runtime: 72 ms, faster than 89.93% of Python3 online submissions for Remove Linked List Elements.
    Memory Usage: 16.5 MB, less than 43.18% of Python3 online submissions for Remove Linked List Elements.
    """
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode(None)
        dummy_head.next = head

        prev = dummy_head
        while prev.next is not None:
            cur = prev.next
            if cur.val == val:
                prev.next = cur.next
                cur = None
            else:
                prev = prev.next

        return dummy_head.next
