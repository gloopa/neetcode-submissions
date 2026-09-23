class Solution:
    def isValid(self, s: str) -> bool:

        close = {')': '(', ']':'[', '}': '{'} 
        stack = []
        for i, char in enumerate(s):
            if char in close and len(stack) > 0:
                if stack[-1] == close[char]:
                    stack.pop() 
                else:
                    return False 
            else:
                stack.append(char)
        
        if len(stack) == 0:
            return True
        else:
            return False
        


        