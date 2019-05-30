#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (32.77%)
# Likes:    817
# Dislikes: 72
# Total Accepted:    182K
# Total Submissions: 550.9K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
# 
# Example 1:
# 
# 
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
# 
# 
# Example 2:
# 
# 
# Input: 1->1->1->2->3
# Output: 2->3
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # My solution 
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        nodes = []
        cur = head
        while cur:
            if not cur.next or cur.val != cur.next.val:
                nodes.append(cur)
                cur = cur.next
            elif cur.next and cur.val == cur.next.val:
                value = cur.val
                while cur and cur.val == value:
                    cur = cur.next
        dummy = ListNode(None)
        tmp = dummy
        for n in nodes + [None]:
            tmp.next = n
            tmp = n
        return dummy.next
    
    # Most-voted solution
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = pre = ListNode(None)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        return dummy.next
