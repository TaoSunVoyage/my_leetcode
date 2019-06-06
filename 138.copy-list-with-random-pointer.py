#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (26.70%)
# Likes:    1559
# Dislikes: 422
# Total Accepted:    248K
# Total Submissions: 911.9K
# Testcase Example:  '{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}'
#
# A linked list is given such that each node contains an additional random
# pointer which could point to any node in the list or null.
# 
# Return a deep copy of the list.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input:
# 
# {"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}
# 
# Explanation:
# Node 1's value is 1, both of its next and random pointer points to Node 2.
# Node 2's value is 2, its next pointer points to null and its random pointer
# points to itself.
# 
# 
# 
# 
# Note:
# 
# 
# You must return the copy of the given head as a reference to the cloned
# list.
# 
# 
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""

from collections import defaultdict
class Solution:
    # My solution
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: 
            return None
        curCopy = headCopy = Node(None, None, None)
        lastCurCopy = Node(None, curCopy, None)
        cur = head
        mapper = {}
        while cur:
            curCopy.val = cur.val
            lastCurCopy.next = curCopy
            if cur.random:
                mapper[cur.random] = mapper.get(cur.random, []) + [curCopy]
            lastCurCopy = curCopy
            cur = cur.next
            curCopy = Node(None, None, None)
        cur, curCopy = head, headCopy
        while cur:
            if cur in mapper:
                while mapper[cur]:
                    mapper[cur].pop().random = curCopy
            cur, curCopy = cur.next, curCopy.next
        return headCopy
    
    # with dict O(2N)
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic = {}
        m = n = head
        while m:
            dic[m] = Node(m.val, None, None)
            m = m.next
        while n:
            dic[n].next = dic.get(n.next)
            dic[n].random = dic.get(n.random)
            n = n.next
        return dic.get(head)
    
    # with dict O(N)
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic = defaultdict(lambda: Node(None, None, None))
        dic[None] = None
        n = head
        while n:
            dic[n].val = n.val
            dic[n].next = dic[n.next]
            dic[n].random = dic[n.random]
            n = n.next
        return dic[head]
    
    # Most-voted
    def copyRandomList(self, head: 'Node') -> 'Node':
        # 1 -> 1' -> 2 -> 2' -> ...
        cur = head
        while cur:
            copy = Node(cur.val, cur.next, None)
            cur.next = copy
            cur = copy.next
        # copy the random pointer
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # break the list into two
        dummy = Node(None, None, None)
        copy = copyCur = dummy
        cur = head
        while cur:
            # extract the copy list
            copy = cur.next
            copyCur.next = copy
            copyCur = copy
            # recover the orignial list
            cur.next = cur.next.next
            cur = cur.next
        return dummy.next

            