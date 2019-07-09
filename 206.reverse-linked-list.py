#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (54.12%)
# Likes:    2460
# Dislikes: 65
# Total Accepted:    619.3K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3,4,5]'
#
# Reverse a singly linked list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# 
# 
# Follow up:
# 
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # My solution - recursively
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        reversedTail = self.reverseList(head.next)
        cur = reversedTail
        while cur.next:
            cur = cur.next
        cur.next = head
        head.next = None
        return reversedTail
    
    # My solution - iteratively
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev



