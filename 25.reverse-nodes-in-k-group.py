#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # my solution
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # dummy node
        dummy = ListNode(None)
        dummy.next = head
        # two pointer
        l = r = dummy
        # save visited nodes
        nodes = []
        while r:
            r = r.next
            if len(nodes) < k:
                nodes.append(r)
            else:
                # reverse
                while nodes:
                    l.next = nodes.pop()
                    l = l.next
                # connect  
                l.next, r = r, l
        return dummy.next
