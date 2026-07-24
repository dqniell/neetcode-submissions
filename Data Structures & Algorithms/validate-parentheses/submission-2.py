class Solution:
    def isValid(self, s: str) -> bool:
        sett = { '(' : ')', '{' : '}', '[' : ']'}
        stack = []

        for bracket in s:
            if bracket in sett:
                stack.append(bracket)
            else: 
                if stack and sett[stack[-1]] == bracket: 
                    stack.pop()
                else: 
                    return False
        return True if not stack else False