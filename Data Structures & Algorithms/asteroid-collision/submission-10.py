class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = [] 

        # [-10]
        for ast in asteroids:

            while stack and stack[-1] > 0 and ast < 0: # + >< - 
                if abs(stack[-1]) < abs(ast):
                    stack.pop() 
                
                elif abs(stack[-1]) == abs(ast):
                    stack.pop()
                    ast = 0 
                
                else:
                    ast = 0
            
            if ast != 0:
                stack.append(ast)
        
        return stack
            

                



        