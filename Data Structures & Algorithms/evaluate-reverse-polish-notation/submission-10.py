class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = set("+-*/")

        stack = []
        
        for token in tokens:
            if token in operations:
                right = stack.pop()
                left = stack.pop()

                if token == '+':
                    result = left + right
                elif token == '-':
                    result = left - right
                elif token == '*':
                    result = left * right
                else:
                    result = int(left / right)

                stack.append(result)

            else:
                stack.append(int(token)) 
       
        return stack[0]
        
        


        
        