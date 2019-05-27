#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
# https://leetcode.com/problems/rotate-list/description/
#
# algorithms
# Medium (26.95%)
# Likes:    594
# Dislikes: 810
# Total Accepted:    191.7K
# Total Submissions: 707K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, rotate the list to the right by k places, where k is
# non-negative.
# 
# Example 1:
# 
# 
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
# 
# 
# Example 2:
# 
# 
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # My Solution
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return head
        cur, count = head, 0
        while cur:
            cur = cur.next
            count += 1
        k = k % count
        if not k: return head
        # dummy
        left = right = ListNode(None)
        right.next = head
        for _ in range(k):
            right = right.next
        left.next = head
        while right.next:
            left = left.next
            right = right.next
        # rotate
        newHead = left.next
        left.next = None
        right.next = head
        return newHead


