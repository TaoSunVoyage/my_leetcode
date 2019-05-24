#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (37.97%)
# Likes:    1559
# Dislikes: 31
# Total Accepted:    177.6K
# Total Submissions: 463.2K
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# Implement a trie with insert, search, and startsWith methods.
# 
# Example:
# 
# 
# Trie trie = new Trie();
# 
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
# 
# 
# Note:
# 
# 
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.
# 
# 
#

# My solution
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isWordEnding = False   # if word ends in the node
        self.children = {}  # 26 pointers

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if not word:
            self.isWordEnding = True
        else:
            if word[0] not in self.children:
                self.children[word[0]] = Trie()
            self.children[word[0]].insert(word[1:])
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if not word: 
            return self.isWordEnding
        if word[0] in self.children:
            return self.children[word[0]].search(word[1:])
        else:
            return False
    

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if not prefix:
            return True
        if prefix[0] in self.children:
            return self.children[prefix[0]].startsWith(prefix[1:])
        else:
            return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

