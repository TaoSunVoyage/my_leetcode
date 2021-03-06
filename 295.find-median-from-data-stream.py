#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#
# https://leetcode.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (36.09%)
# Likes:    1226
# Dislikes: 24
# Total Accepted:    113.9K
# Total Submissions: 305.9K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n[[],[1],[2],[],[3],[]]'
#
# Median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value. So the median is the mean of the two
# middle value.
# For example,
# 
# [2,3,4], the median is 3
# 
# [2,3], the median is (2 + 3) / 2 = 2.5
# 
# Design a data structure that supports the following two operations:
# 
# 
# void addNum(int num) - Add a integer number from the data stream to the data
# structure.
# double findMedian() - Return the median of all elements so far.
# 
# 
# 
# 
# Example:
# 
# 
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2
# 
# 
# 
# 
# Follow up:
# 
# 
# If all integer numbers from the stream are between 0 and 100, how would you
# optimize it?
# If 99% of all integer numbers from the stream are between 0 and 100, how
# would you optimize it?
# 
# 
#
import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = [] # min heap -> larger half
        self.maxHeap = [] # max heap -> smaller half
        
    def addNum(self, num: int) -> None:
        # balance two heaps
        if len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappushpop(self.minHeap, num))
        else:
            heapq.heappush(self.minHeap, -heapq.heappushpop(self.maxHeap, -num))

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return (self.minHeap[0] - self.maxHeap[0]) / 2

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

