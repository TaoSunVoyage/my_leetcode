#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
class Solution:
    # my solution
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        def add(digit: str, combinations: List[str]) -> List[str]:
            alphabeta = digit_map[digit]
            new_combinations = []
            if not combinations:
                return list(alphabeta)
            for ab in alphabeta:
                for c in combinations:
                    new_combinations.append(c + ab)
            return new_combinations
        
        combinations = []
        for d in digits:
            combinations = add(d, combinations)
        
        return combinations
    
    # top-voted
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(mapping[digits[0]])
        # Backtracking
        # Start from the last element
        prev = self.letterCombinations(digits[:-1])
        additional = mapping[digits[-1]]
        return [s + c for s in prev for c in additional]
        

