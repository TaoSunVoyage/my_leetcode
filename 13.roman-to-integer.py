#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#
class Solution:
    def romanToInt(self, s: str) -> int:
        s_v = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 
            'C': 100, 'D': 500, 'M': 1000
        }
        num = 0
        length = len(s)
        for i in range(length):
            if i != length - 1:
                if s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X'):
                    add = - s_v[s[i]]
                elif s[i] == 'X' and (s[i+1] == 'L' or s[i+1] == 'C'):
                    add = - s_v[s[i]]
                elif s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'):
                    add = - s_v[s[i]]
                else:
                    add = s_v[s[i]]
            else:
                add = s_v[s[i]]
            num += add
        return num



