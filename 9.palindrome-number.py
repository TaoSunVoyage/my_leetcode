#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
class Solution:
    def isPalindrome(self, x: int) -> bool:
        l = list(str(x))
        if l[0] == '-':
            return False
        for i in range(len(l)):
            j = len(l) - i - 1
            if j <= i:
                break
            if l[i] != l[j]:
                return False
        return True

