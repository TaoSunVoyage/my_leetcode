#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#
# https://leetcode.com/problems/valid-number/description/
#
# algorithms
# Hard (13.95%)
# Likes:    424
# Dislikes: 3155
# Total Accepted:    123.6K
# Total Submissions: 883.3K
# Testcase Example:  '"0"'
#
# Validate if a given string can be interpreted as a decimal number.
# 
# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# " -90e3   " => true
# " 1e" => false
# "e3" => false
# " 6e-1" => true
# " 99e2.5 " => false
# "53.5e93" => true
# " --6 " => false
# "-+3" => false
# "95a54e53" => false
# 
# Note: It is intended for the problem statement to be ambiguous. You should
# gather all requirements up front before implementing one. However, here is a
# list of characters that can be in a valid decimal number:
# 
# 
# Numbers 0-9
# Exponent - "e"
# Positive/negative sign - "+"/"-"
# Decimal point - "."
# 
# 
# Of course, the context of these characters also matters in the input.
# 
# Update (2015-02-10):
# The signature of the C++ function had been updated. If you still see your
# function signature accepts a const char * argument, please click the reload
# button to reset your code definition.
# 
#
class Solution:
    # Most voted solution
    def isNumber(self, s: str) -> bool:
        #Deterministic Finite Automaton
        state = [
            {}, 
            {'blank':1, 'sign': 2, 'digit':3, '.':4}, 
            {'digit':3, '.':4},
            {'digit':3, '.':5, 'e':6, 'blank':9},
            {'digit':5},
            {'digit':5, 'e':6, 'blank':9},
            {'sign':7, 'digit':8},
            {'digit':8},
            {'digit':8, 'blank':9},
            {'blank':9}
        ]
        currentState = 1
        for c in s:
            if c >= '0' and c <= '9':
                c = 'digit'
            if c == ' ':
                c = 'blank'
            if c in ['+', '-']:
                c = 'sign'
            if c not in state[currentState]:
                return False
            currentState = state[currentState][c]
        return currentState in [3,5,8,9]

                

