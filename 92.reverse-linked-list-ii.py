#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (34.66%)
# Likes:    1251
# Dislikes: 92
# Total Accepted:    198.8K
# Total Submissions: 565K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Reverse a linked list from position m to n. Do it in one-pass.
# 
# Note: 1 ≤ m ≤ n ≤ length of list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = cur = ListNode(None)
        cur.next = head
        
        for _ in range(m - 1):
            cur = cur.next
        # the node before the interval
        before = cur
        # nodes in the interval
        nodes = []
        for i in range(n - m + 1):
            cur = cur.next
            nodes.append(cur)
        # the node after the interval
        after = cur.next
        # reconnect
        for n in nodes[::-1]:
            before.next = n
            before = n
        before.next = after

        return dummy.next     

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = cur = ListNode(None)
        cur.next = head
        for _ in range(m - 1):
            cur = cur.next
        # the node before the interval
        before = cur
        # reverse nodes between [m, n]
        nodeBefore = None
        cur = cur.next
        for _ in range(n - m + 1):
            nodeAfter = cur.next
            cur.next = nodeBefore
            nodeBefore = cur
            cur = nodeAfter
        # connect
        before.next.next = cur
        before.next = nodeBefore

        return dummy.next

