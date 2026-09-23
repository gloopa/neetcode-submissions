class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = [] 
        ops = set("+DC")

        for op in operations:
            if op not in ops:
                stack.append(int(op)) 
            if op == "+":
                stack.append(sum(stack[-2:])) 
            if op == "C":
                stack.pop() 
            if op == "D":
                stack.append(2 * stack[-1])
            
            
            

        return sum(stack)