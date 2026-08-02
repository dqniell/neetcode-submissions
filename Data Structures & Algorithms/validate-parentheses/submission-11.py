class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        stack = deque()

        mapp = {
            ')' : '(', 
            '}' : '{', 
            ']' : '[' 
        }

        for char in s: 
            if char in mapp: 
                if stack and stack[-1] == mapp[char]: 
                    stack.pop()
                else: 
                    return False
            else: 
                stack.append(char)
        
        return False if stack else True