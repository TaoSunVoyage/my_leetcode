#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (36.96%)
# Likes:    657
# Dislikes: 179
# Total Accepted:    164.5K
# Total Submissions: 440.9K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given a linked list and a value x, partition it such that all nodes less than
# x come before nodes greater than or equal to x.
# 
# You should preserve the original relative order of the nodes in each of the
# two partitions.
# 
# Example:
# 
# 
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5
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
    def partition(self, head: ListNode, x: int) -> ListNode:
        less = []
        greater = []
        cur = head
        while cur:
            if cur.val < x:
                less.append(cur.val)
            else:
                greater.append(cur.val)
            cur = cur.next
        dummy = ListNode(None)
        cur = dummy
        for n in less + greater:
            cur.next = ListNode(n)
            cur = cur.next
        return dummy.next
    # My solution
    def partition(self, head: ListNode, x: int) -> ListNode:
        lessCur = lessDummy = ListNode(None)
        greaterCur = greaterDummy = ListNode(None)
        cur = head
        while cur:
            if cur.val < x:
                lessCur.next = cur
                lessCur = lessCur.next
            else:
                greaterCur.next = cur
                greaterCur = greaterCur.next
            cur = cur.next
        greaterCur.next = None
        lessCur.next = greaterDummy.next
        return lessDummy.next

