class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left =0
        right = len(numbers)-1
        while left<=right:
            value = numbers[right] + numbers[left]
            if value == target:
                return [left+1, right+1]
            if value < target:
                left+=1
            else:
                right-=1
    
        