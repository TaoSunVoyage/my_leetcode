#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#
class Solution:
    # used * and / ...
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0: return 0
        neg = (dividend > 0) ^ (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        while dividend >= divisor:
            temp = dividend
            i = 1
            while temp >= divisor:
                temp -= i * divisor
                i *= 2
            quotient += i/2
            dividend -= i/2 * divisor
        quotient = -quotient if neg else quotient
        return min(max(-2147483648, int(quotient)), 2147483647)
    
    # without *, / or %
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0: return 0
        neg = (dividend > 0) ^ (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        while dividend >= divisor:
            temp = divisor
            i = 1
            while dividend >= temp:
                dividend -= temp
                quotient += i
                i <<= 1
                temp <<= 1
        quotient = -quotient if neg else quotient
        return min(max(-2147483648, int(quotient)), 2147483647)

