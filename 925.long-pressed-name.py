#
# @lc app=leetcode id=925 lang=python3
#
# [925] Long Pressed Name
#
# https://leetcode.com/problems/long-pressed-name/description/
#
# algorithms
# Easy (44.36%)
# Likes:    300
# Dislikes: 40
# Total Accepted:    22.6K
# Total Submissions: 50.8K
# Testcase Example:  '"alex"\n"aaleex"'
#
# Your friend is typing his name into a keyboard.  Sometimes, when typing a
# character c, the key might get long pressed, and the character will be typed
# 1 or more times.
# 
# You examine the typed characters of the keyboard.  Return True if it is
# possible that it was your friends name, with some characters (possibly none)
# being long pressed.
# 
# 
# 
# Example 1:
# 
# 
# Input: name = "alex", typed = "aaleex"
# Output: true
# Explanation: 'a' and 'e' in 'alex' were long pressed.
# 
# 
# 
# Example 2:
# 
# 
# Input: name = "saeed", typed = "ssaaedd"
# Output: false
# Explanation: 'e' must have been pressed twice, but it wasn't in the typed
# output.
# 
# 
# 
# Example 3:
# 
# 
# Input: name = "leelee", typed = "lleeelee"
# Output: true
# 
# 
# 
# Example 4:
# 
# 
# Input: name = "laiden", typed = "laiden"
# Output: true
# Explanation: It's not necessary to long press any character.
# 
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# name.length <= 1000
# typed.length <= 1000
# The characters of name and typed are lowercase letters.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        def characterCount(str):
            strCounter = []
            character = str[0]
            count = 1
            for i in range(1, len(str)):
                if str[i] == character:
                    count += 1
                else:
                    strCounter.append((character, count))
                    character = str[i]
                    count = 1
            strCounter.append((character, count))
            return strCounter
        
        nameCounter = characterCount(name)
        typedCounter = characterCount(typed)

        if len(nameCounter) != len(typedCounter):
            return False

        for a, b in zip(nameCounter, typedCounter):
            if a[0] != b[0] or a[1] > b[1]:
                return False
        
        return True

    # Most-voted
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        if len(typed) < len(name):
            return False
        if typed == name:
            return True
        
        while i < len(name):
            if name[i] == typed[j]:
                i += 1
                j += 1
            else:
                j += 1
            if j == len(typed) and i != len(name):
                return False
        
        return True

# @lc code=end

