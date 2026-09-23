class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        count=0
        res = 0
        for num in numbers:
            if num-1 not in numbers: #new start 
                count=1 #initialize
                while num+count in numbers:
                    count+=1 
                res = max(res, count)
        return res




                    
                    



                
            
      
        return val

        
        