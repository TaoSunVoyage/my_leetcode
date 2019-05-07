#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ''
        n_strs = len(strs)
        if not n_strs:
            return pre
        min_len = min([len(s) for s in strs])
        for i in range(min_len):
            letters = list(set(s[i] for s in strs))
            if len(letters) == 1:
                pre += letters[0]
            else:
                break
        return pre
    
    # Elegant solution
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     sz, ret = zip(*strs), ""
    #     for c in sz:
    #         if len(set(c)) > 1: break
    #         ret += c[0]
    #     return ret

