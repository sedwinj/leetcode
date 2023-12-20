# https://leetcode.com/problems/add-two-numbers

from typing import Optional


class ListNode:
    """
    Definition for singly-linked list.
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach:
                  1. Traverse each list, adding the sum of digits (and carry) to an array.
                  2. Traverse the array backwards, adding elements to a new list. Return the list.

                  O(n)

                  Arrays are faster than linked lists because of sequential access. This makes them
                  better as an intermediary.
        """

        array = []
        carry = 0

        # Sum two linked lists element-wise
        while l1 is not None and l2 is not None:
            _sum = l1.val + l2.val + carry
            carry = _sum // 10
            array.append(_sum % 10)
            l1 = l1.next
            l2 = l2.next

        # Sum any excess with the carry
        excess = l1 if l2 is None else l2
        while excess is not None:
            _sum = excess.val + carry
            carry = _sum // 10
            array.append(_sum % 10)
            excess = excess.next

        # Don't forget the carry!
        if carry > 0:
            array.append(carry)

        # Conversion back to linked list
        head = None
        for num in reversed(array):
            head = ListNode(num, head)

        return head
