class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        temp = []

        def back(start, tar):
            if tar == 0:
                result.append(temp[:])
                return 
            
            for i in range(start, len(nums)):
                if nums[i] > tar:
                    break #everything else is also gonna be greater than target value since we sorted it
                temp.append(nums[i])
                back(i, tar - nums[i]) #subtracts each time, our goal is to reach 0
                temp.pop()
        back(0, target)
        return result
        