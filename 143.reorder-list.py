#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#
# https://leetcode.com/problems/reorder-list/description/
#
# algorithms
# Medium (30.50%)
# Likes:    899
# Dislikes: 65
# Total Accepted:    158.1K
# Total Submissions: 507.6K
# Testcase Example:  '[1,2,3,4]'
#
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# 
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
# 
# Example 1:
# 
# 
# Given 1->2->3->4, reorder it to 1->4->2->3.
# 
# Example 2:
# 
# 
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return 
        # find the mid
        l, r = head, head
        length = 1
        while r and r.next:
            l = l.next
            r = r.next.next
            length += 1
        # get the second half
        secondHalf = l.next
        l.next = None
        # reverse second half
        secondHalf = self.reverseList(secondHalf)
        # combine two lists
        firstHalf = head
        while secondHalf:
            firstTemp, secondTemp = firstHalf.next, secondHalf.next
            
            firstHalf.next, firstHalf.next.next = secondHalf, firstTemp
            
            firstHalf, secondHalf = firstTemp, secondTemp

    def reverseList(self, head):
        l = []
        while head:
            l.append(head)
            head = head.next
        dummy = cur = ListNode(None)
        for n in reversed(l):
            cur.next = n
            cur = n
        cur.next = None
        return dummy.next


