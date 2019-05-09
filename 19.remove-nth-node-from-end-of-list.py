#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # my first solution
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = cursor = ListNode(None)
        # two pointers
        l = r = head
        for _ in range(n - 1):
            r = r.next
        # loop to the next
        while r.next:
            cursor.next = l
            cursor = cursor.next
            l = l.next
            r = r.next
        # skip the nth element
        cursor.next = l.next
        return dummy.next
    
    # # No dummy node
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    #     fast = slow = head
    #     for _ in range(n):
    #         fast = fast.next
    #     if not fast:
    #         return head.next
    #     while fast.next:
    #         fast = fast.next
    #         slow = slow.next
    #     slow.next = slow.next.next
    #     return head
