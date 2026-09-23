class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        temp=[]
        n =len(nums)

        def back(i):
        
            result.append(temp[:])
            for j in range(i, n):
                if nums[j-1] == nums[j] and j>i:
                    continue
                temp.append(nums[j])
                back(j+1)
                temp.pop()
            
        back(0)
        return result
                

                 

        
        