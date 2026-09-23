class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = Counter(nums)
        for num,fre in freq.items():
            if fre >=2:
                return num
        
            
        