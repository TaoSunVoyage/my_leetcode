#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (23.44%)
# Likes:    506
# Dislikes: 864
# Total Accepted:    131.4K
# Total Submissions: 558.8K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# You are given a string, s, and a list of words, words, that are all of the
# same length. Find all starting indices of substring(s) in s that is a
# concatenation of each word in words exactly once and without any intervening
# characters.
#
# Example 1:
#
#
# Input:
# ⁠ s = "barfoothefoobarman",
# ⁠ words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar"
# respectively.
# The output order does not matter, returning [9,0] is fine too.
#
#
# Example 2:
#
#
# Input:
# ⁠ s = "wordgoodgoodgoodbestword",
# ⁠ words = ["word","good","best","word"]
# Output: []
#
#
#


class Solution:
    # my solution
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not s: return []
        
        lengthWord, nWord = len(words[0]), len(words)
        
        wordCount = {}
        for w in words:
            wordCount[w] = wordCount.get(w, 0) + 1

        result = []

        for k in range(len(s) - nWord * lengthWord + 1):
            word = s[k: k + lengthWord]
            if word not in wordCount:
                continue
            wordFoundCount = {word: 1}
            count = 1
            nextK = k + lengthWord
            while count < nWord:
                word = s[nextK: nextK + lengthWord]
                if word not in wordCount:
                    break
                wordFoundCount[word] = wordFoundCount.get(word, 0) + 1
                if wordCount[word] < wordFoundCount[word]:
                    break
                count += 1
                nextK += lengthWord
            else:
                result.append(k)
        return result

