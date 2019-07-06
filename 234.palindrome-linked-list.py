#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (35.82%)
# Likes:    1714
# Dislikes: 253
# Total Accepted:    270.1K
# Total Submissions: 742.7K
# Testcase Example:  '[1,2]'
#
# Given a singly linked list, determine if it is a palindrome.
# 
# Example 1:
# 
# 
# Input: 1->2
# Output: false
# 
# Example 2:
# 
# 
# Input: 1->2->2->1
# Output: true
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # My solution - O(N) time, O(1) space
    def isPalindrome(self, head: ListNode) -> bool:
        cur, count = head, 0
        while cur:
            count += 1
            cur = cur.next
        first = second = head
        for _ in range((count - 1) // 2 + 1):
            second = second.next
        second = self.reverseList(second)
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True
    
    def reverseList(self, head):
        prev = None
        current = head 
        while current: 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        head = prev
        return head
    
    # Most-voted
    def isPalindrome(self, head):
        # Phase 1: Reverse the first half while finding the middle.
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        # Phase 2: Compare the reversed first half with the second half.
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev


