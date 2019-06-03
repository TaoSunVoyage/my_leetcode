#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#
# https://leetcode.com/problems/min-stack/description/
#
# algorithms
# Easy (36.61%)
# Likes:    1759
# Dislikes: 184
# Total Accepted:    302.6K
# Total Submissions: 815.8K
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]]'
#
# 
# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.
# 
# 
# push(x) -- Push element x onto stack.
# 
# 
# pop() -- Removes the element on top of the stack.
# 
# 
# top() -- Get the top element.
# 
# 
# getMin() -- Retrieve the minimum element in the stack.
# 
# 
# 
# 
# Example:
# 
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.
# 
# 
#
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minValue = [ ]
        

    def push(self, x: int) -> None:
        self.stack.insert(0, x)
        if not self.minValue or x <= self.minValue[0]:
            self.minValue.insert(0, x)

    def pop(self) -> None:
        x = self.stack.pop(0)
        if x == self.getMin():
            _ = self.minValue.pop(0)

    def top(self) -> int:
        if not self.stack: 
            return None
        return self.stack[0]

    def getMin(self) -> int:
        if not self.minValue:
            return None
        return self.minValue[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

