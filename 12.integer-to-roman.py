#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ''
        # translate
        q, num = num // 1000, num % 1000
        roman += 'M' * q
        q, num = num // 100, num % 100
        roman += 'C' * q
        q, num = num // 10, num % 10
        roman += 'X' * q
        roman += 'I' * num
        # replace
        roman = roman.replace('C' * 9, 'CM')
        roman = roman.replace('C' * 5, 'D')
        roman = roman.replace('C' * 4, 'CD')
        roman = roman.replace('X' * 9, 'XC')
        roman = roman.replace('X' * 5, 'L')
        roman = roman.replace('X' * 4, 'XL')
        roman = roman.replace('I' * 9, 'IX')
        roman = roman.replace('I' * 5, 'V')
        roman = roman.replace('I' * 4, 'IV')
        return roman
    
    # easy way
    # def intToRoman(self, num: int) -> str:
    #     M = ["", "M", "MM", "MMM"]
    #     C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    #     X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    #     I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    #     return M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10]


