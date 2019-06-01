#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder/description/
#
# algorithms
# Medium (23.70%)
# Likes:    1425
# Dislikes: 797
# Total Accepted:    258.6K
# Total Submissions: 1.1M
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# the length of shortest transformation sequence from beginWord to endWord,
# such that:
# 
# 
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
# 
# 
# Note:
# 
# 
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# 
# 
# Example 1:
# 
# 
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# Output: 5
# 
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" ->
# "dog" -> "cog",
# return its length 5.
# 
# 
# Example 2:
# 
# 
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# Output: 0
# 
# Explanation: The endWord "cog" is not in wordList, therefore no possible
# transformation.
# 
# 
# 
# 
# 
#
from collections import defaultdict
class Solution:
    # My solution - TLE 
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        wordList.insert(0, beginWord)
        graph = {w: [] for w in wordList}
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                w1 = wordList[i]
                w2 = wordList[j]
                if self.validPath(w1, w2):
                    graph[w1].append(w2)
                    graph[w2].append(w1)
        
        return self.bfs(graph, beginWord, endWord)

    def validPath(self, word1, word2):
        diff = 0
        for c1, c2 in zip(word1, word2):
            diff += c1 != c2
        return diff == 1
    
    def bfs(self, graph, beginWord, endWord):
        toSearch = [beginWord]
        visited = []
        level = 0
        while toSearch:
            level += 1
            nextToSearch = []
            for w in toSearch:
                if w == endWord:
                    return level
                nextToSearch += graph[w]
            visited += toSearch
            toSearch = [w for w in nextToSearch if w not in visited]
        return 0

    def dfs(self, graph, beginWord, endWord):
        def helper(graph, start, target, path):
            if target in graph[start]:
                path.append(target)
                return len(path)
            nextWord = [w for w in graph[start] if w not in path]
            if not nextWord:
                return 0
            shortest = 0
            for w in nextWord:
                length = helper(graph, w, target, path + [w])
                if not shortest:
                    shortest = length
                elif length:
                    shortest = min(shortest, length)
            return shortest
        return helper(graph, beginWord, endWord, [beginWord])



    # Most-voted solution
    # BFS is better than DFS here
    # How to construct the graph is very important here
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)


        # Queue for BFS
        queue = [(beginWord, 1)]
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.pop(0)      
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0

