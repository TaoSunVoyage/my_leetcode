#
# @lc app=leetcode id=211 lang=python3
#
# [211] Add and Search Word - Data structure design
#
# https://leetcode.com/problems/add-and-search-word-data-structure-design/description/
#
# algorithms
# Medium (29.98%)
# Likes:    809
# Dislikes: 51
# Total Accepted:    114K
# Total Submissions: 376.9K
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# Design a data structure that supports the following two operations:
# 
# 
# void addWord(word)
# bool search(word)
# 
# 
# search(word) can search a literal word or a regular expression string
# containing only letters a-z or .. A . means it can represent any one letter.
# 
# Example:
# 
# 
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# 
# 
# Note:
# You may assume that all words are consist of lowercase letters a-z.
# 
#

# My Solution
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isWordEnd = False
        self.children = {}
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        wordDict = self
        for c in word:
            if c not in wordDict.children:
                wordDict.children[c] = WordDictionary()
            wordDict = wordDict.children[c]
        wordDict.isWordEnd = True
            

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        wordDicts = [self]
        for c in word:
            nextWordDicts = []
            if c == '.':
                for d in wordDicts:
                    nextWordDicts += d.children.values()
            else:
                for d in wordDicts:
                    if c in d.children:
                        nextWordDicts.append(d.children[c])
            if not nextWordDicts:
                return False
            wordDicts = nextWordDicts
        res = False
        for d in wordDicts:
            res |= d.isWordEnd
        return res
            

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

