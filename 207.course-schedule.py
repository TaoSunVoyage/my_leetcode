#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (37.46%)
# Likes:    1718
# Dislikes: 83
# Total Accepted:    213.4K
# Total Submissions: 565.4K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, is it
# possible for you to finish all courses?
# 
# Example 1:
# 
# 
# Input: 2, [[1,0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# Example 2:
# 
# 
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should
# also have finished course 1. So it is impossible.
# 
# 
# Note:
# 
# 
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 
# 
#
class Solution:
    # My solution
    # Time Limit Exceeded
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = dict()
        for c1, c2 in prerequisites:
            adj[c1] = adj.get(c1, []) + [c2]
        
        for c in adj:
            visited = []
            self.dfs(c, adj, visited)
            if c in visited:
                return False
        return True

    def dfs(self, start, graph, visited):
        for c in graph.get(start, []):
            if c not in visited:
                visited.append(c)
                self.dfs(c, graph, visited)

    # Most-voted solution
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        def dfs(i):
            if visited[i] == -1:
                return False
            if visited[i] == 1:
                return True
            visited[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visited[i] = 1
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

