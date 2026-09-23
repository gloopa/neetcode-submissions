class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort = sorted(nums)
        result = []

        for i in range(len(sort)):
            if i>0 and sort[i] == sort[i-1]:
                continue 
            left = i+1
            right = len(sort) - 1
            while left<right:
                val = sort[i] + sort[left] + sort[right]
                if val == 0:
                    result.append((sort[i], sort[left], sort[right]))
                    left+=1
                    right-=1
                    while left<right and sort[left] == sort[left-1]:
                        left+=1
                    while left<right and sort[right]== sort[right+1]:
                        right-=1
                elif val < 0:
                    left+=1 
                else:
                    right-=1
        
        return result
        