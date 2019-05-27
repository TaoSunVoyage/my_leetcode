#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
# https://leetcode.com/problems/insert-interval/description/
#
# algorithms
# Hard (31.08%)
# Likes:    805
# Dislikes: 98
# Total Accepted:    176.6K
# Total Submissions: 565.8K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# Given a set of non-overlapping intervals, insert a new interval into the
# intervals (merge if necessary).
# 
# You may assume that the intervals were initially sorted according to their
# start times.
# 
# Example 1:
# 
# 
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# 
# 
# Example 2:
# 
# 
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with
# [3,5],[6,7],[8,10].
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#
class Solution:
    # My solution
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out = []
        for i, interval in enumerate(intervals):
            # insert interval
            if interval[1] < newInterval[0]:
                out.append(interval)
            # insert new interval
            elif newInterval[1] < interval[0]:
                out.append(newInterval)
                out += intervals[i:]
                break
            # update new interval
            else:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
        # if there is no break -> new interval hasn't been inserted
        else:
            out.append(newInterval)
        return out
    
    # Most-voted Solution
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval[0], newInterval[1]
        left = [i for i in intervals if i[1] < s]
        right = [i for i in intervals if i[0] > e]
        if len(left) + len(right) != len(intervals):
            s = min(s, intervals[len(left)][0])
            e = max(e, intervals[~len(right)][1])
        return left + [[s, e]] + right

