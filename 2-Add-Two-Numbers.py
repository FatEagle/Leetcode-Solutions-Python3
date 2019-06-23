# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Runtime: 92 ms, faster than 27.57% of Python3 online submissions for Add Two Numbers.
    Memory Usage: 13.4 MB, less than 12.52% of Python3 online submissions for Add Two Numbers.

    Test cases:
    [2,4,3]
    [5,6,4]
    [0]
    [0]
    [5]
    [5]
    [9, 9, 9]
    [1]
    """

    @staticmethod
    def add(a, b, curry):
        q = a + b + curry
        if q >= 10:
            q = q % 10
            r = 1
        else:
            r = 0
        return q, r

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1 = l1
        cur2 = l2

        q, curry = self.add(cur1.val, cur2.val, 0)
        result = ListNode(q)
        cur1 = cur1.next
        cur2 = cur2.next

        head = result
        while cur1 is not None and cur2 is not None:
            value1 = cur1.val
            value2 = cur2.val

            q, curry = self.add(value1, value2, curry)
            result.next = ListNode(q)
            result = result.next

            cur1 = cur1.next
            cur2 = cur2.next

        if cur1 is None and cur2 is None:
            if curry == 1:
                result.next = ListNode(curry)

        if cur1 is not None:
            q, curry = self.add(cur1.val, curry, 0)
            result.next = ListNode(q)
            result = result.next
            cur1 = cur1.next

            while cur1 is not None:
                q, curry = self.add(cur1.val, curry, 0)
                result.next = ListNode(q)
                result = result.next
                cur1 = cur1.next

            if curry == 1:
                result.next = ListNode(curry)

        if cur2 is not None:
            q, curry = self.add(cur2.val, curry, 0)
            result.next = ListNode(q)
            result = result.next
            cur2 = cur2.next

            while cur2 is not None:
                q, curry = self.add(cur2.val, curry, 0)
                result.next = ListNode(q)
                result = result.next
                cur2 = cur2.next

            if curry == 1:
                result.next = ListNode(curry)

        return head
