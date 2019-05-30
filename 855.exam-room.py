#
# @lc app=leetcode id=855 lang=python3
#
# [855] Exam Room
#
# https://leetcode.com/problems/exam-room/description/
#
# algorithms
# Medium (37.90%)
# Likes:    302
# Dislikes: 150
# Total Accepted:    14.6K
# Total Submissions: 38.2K
# Testcase Example:  '["ExamRoom","seat","seat","seat","seat","leave","seat"]\n[[10],[],[],[],[],[4],[]]'
#
# In an exam room, there are N seats in a single row, numbered 0, 1, 2, ...,
# N-1.
# 
# When a student enters the room, they must sit in the seat that maximizes the
# distance to the closest person.  If there are multiple such seats, they sit
# in the seat with the lowest number.  (Also, if no one is in the room, then
# the student sits at seat number 0.)
# 
# Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat()
# returning an int representing what seat the student sat in, and
# ExamRoom.leave(int p) representing that the student in seat number p now
# leaves the room.  It is guaranteed that any calls to ExamRoom.leave(p) have a
# student sitting in seat p.
# 
# 
# 
# Example 1:
# 
# 
# Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"],
# [[10],[],[],[],[],[4],[]]
# Output: [null,0,9,4,2,null,5]
# Explanation:
# ExamRoom(10) -> null
# seat() -> 0, no one is in the room, then the student sits at seat number 0.
# seat() -> 9, the student sits at the last seat number 9.
# seat() -> 4, the student sits at the last seat number 4.
# seat() -> 2, the student sits at the last seat number 2.
# leave(4) -> null
# seat() -> 5, the student sits at the last seat number 5.
# 
# 
# ​​​​​​​
# 
# Note:
# 
# 
# 1 <= N <= 10^9
# ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across
# all test cases.
# Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting
# in seat number p.
# 
# 
#

# My solution
class ExamRoom:

    def __init__(self, N: int):
        self.numberOfSeats = N
        self.seatsOccupied = []
        self.nextSeat = 0

    def seat(self) -> int:
        nextSeat = self.nextSeat
        self.seatsOccupied.append(nextSeat)
        self.seatsOccupied.sort()
        self._updateNextSeat()
        return nextSeat

    def leave(self, p: int) -> None:
        self.seatsOccupied.remove(p)
        self._updateNextSeat()
    
    def _updateNextSeat(self) -> None:
        # self.nextSeat = 0
        # for i in range(len(self.seatsOccupied)):
        #     if i == 0:
        #         maxD = self.seatsOccupied[0]
        #         self.nextSeat = 0
            
        #     if i > 0:
        #         d = (self.seatsOccupied[i] - self.seatsOccupied[i - 1]) // 2
        #         if d > maxD:
        #             maxD = d
        #             self.nextSeat = (self.seatsOccupied[i] + self.seatsOccupied[i - 1]) // 2
                
        #     if i == len(self.seatsOccupied) - 1:
        #         d = self.numberOfSeats - 1 - self.seatsOccupied[i]
        #         if d > maxD:
        #             maxD = d
        #             self.nextSeat = self.numberOfSeats - 1

        if not self.seatsOccupied: 
            self.nextSeat = 0
            return
        preDist = 0
        for i in range(1, len(self.seatsOccupied)):
            dist = (self.seatsOccupied[i] - self.seatsOccupied[i - 1]) // 2
            if dist > preDist:
                self.nextSeat = (self.seatsOccupied[i] + self.seatsOccupied[i - 1]) // 2
                preDist = dist
        if self.seatsOccupied[0] >= preDist:
            self.nextSeat = 0
            preDist = self.seatsOccupied[0]
        if self.numberOfSeats - 1 - self.seatsOccupied[-1] > preDist:
            self.nextSeat = self.numberOfSeats - 1


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)

