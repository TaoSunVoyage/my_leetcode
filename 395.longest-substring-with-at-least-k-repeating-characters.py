#
# @lc app=leetcode id=395 lang=python3
#
# [395] Longest Substring with At Least K Repeating Characters
#
class Solution:
    # # Time Limit Exceeded
    # def longestSubstring(self, s: str, k: int) -> int:
    #     maxlen = 0
    #     for i in range(len(s)):
    #         for j in range(i + 1, len(s) + 1):
    #             substr = s[i:j]
    #             counter = {}
    #             for c in substr:
    #                 if c in counter:
    #                     counter[c] += 1
    #                 else:
    #                     counter[c] = 1
    #             for c in counter:
    #                 if counter[c] < k:
    #                     break
    #             else:
    #                 maxlen = max(maxlen, len(substr))
    #     return maxlen
   
    # python magic?
    def longestSubstring(self, s: str, k: int) -> int:
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(ss, k) for ss in s.split(c))
        return len(s)
    
    # two pointers
    def longestSubstring(self, s: str, k: int) -> int:
        maxlen = 0
        for h in range(1, 27):
            i = j = 0
            noLessThanK = 0
            unique = 0
            counter = [0 for _ in range(26)]
            while j < len(s):
                if unique <= h:
                    idx = ord(s[j]) - ord('a')
                    if counter[idx] == 0:
                        unique += 1
                    counter[idx] += 1
                    if counter[idx] == k:
                        noLessThanK += 1
                    j += 1
                else:
                    idx = ord(s[i]) - ord('a')
                    if counter[idx] == k:
                        noLessThanK -= 1
                    counter[idx] -= 1
                    if counter[idx] == 0:
                        unique -= 1
                    i += 1
                if unique == noLessThanK and unique == h:
                    maxlen = max(maxlen, j - i)
        return maxlen
                        
