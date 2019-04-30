#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
class Solution:
    def reverse(self, x: int) -> int:
        s = list(str(x))
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        s.reverse()
        num = sign * int(''.join(s))
        if num > 2**31 -1 or num < - 2**31:
            return 0
        else:
            return num

