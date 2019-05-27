#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (42.37%)
# Likes:    748
# Dislikes: 78
# Total Accepted:    327K
# Total Submissions: 768.5K
# Testcase Example:  '[1,1,2]'
#
# Given a sorted linked list, delete all duplicates such that each element
# appear only once.
# 
# Example 1:
# 
# 
# Input: 1->1->2
# Output: 1->2
# 
# 
# Example 2:
# 
# 
# Input: 1->1->2->3->3
# Output: 1->2->3
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # My Solution
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return head
        first, second = head, head.next
        while second:
            if second.val != first.val:
                first.next = second
                first, second = second, second.next
            else:
                first.next = second.next
                second = second.next
        return head
    
    # Most-voted Solution
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head


