class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        stack = deque()

        mapp = {
            ')' : '(', 
            '}' : '{', 
            ']' : '[' 
        }

        #so if we go through the string, and if it is a opening bracket, we push to the stack
        #if it is a closing bracket, we need to check if the top of the stack matches, then if so, pop

        for char in s: 
            if char in mapp.values(): 
                stack.append(char)
            else: 
                if stack and char in mapp and stack[-1] == mapp[char]: 
                    stack.pop()
                else: 
                    return False
        
        if stack: 
            return False
        else: 
            return True
