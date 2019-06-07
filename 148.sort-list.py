#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#
# https://leetcode.com/problems/sort-list/description/
#
# algorithms
# Medium (34.91%)
# Likes:    1444
# Dislikes: 75
# Total Accepted:    186.2K
# Total Submissions: 524.9K
# Testcase Example:  '[4,2,1,3]'
#
# Sort a linked list in O(n log n) time using constant space complexity.
# 
# Example 1:
# 
# 
# Input: 4->2->1->3
# Output: 1->2->3->4
# 
# 
# Example 2:
# 
# 
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # O(N^2) time, O(1) space, TLE
    def sortList(self, head: ListNode) -> ListNode:
        n = 0
        cur = head
        # number of nodes
        while cur:
            n += 1
            cur = cur.next
        
        for i in range(n - 1):
            cur = head
            for _ in range(n - 1 - i):
                if cur.val > cur.next.val:
                    cur.val, cur.next.val = cur.next.val, cur.val
                cur = cur.next
        
        return head
    

    # Most-voted solution
    # Merge two sorted lists together
    def merge(self, h1, h2):
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, tail, h1 = h1, h1, h1.next
            else:
                tail.next, tail, h2 = h2, h2, h2.next
    
        tail.next = h1 or h2
        return dummy.next
    
    def sortList(self, head):
        if not head or not head.next:
            return head
    
        # how to get the mid node
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        # break list into two parts
        pre.next = None

        return self.merge(*map(self.sortList, (head, slow)))
    

