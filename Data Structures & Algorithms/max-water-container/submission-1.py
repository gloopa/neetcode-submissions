class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1 
        area = 0
        current_max = 0

        while left<right:
            area = min(heights[left], heights[right]) * (right-left)
            current_max = max(current_max, area)
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        return current_max

    
        

                

      







        