class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sort = sorted(nums1 + nums2)
        #[1,2,3,4]
        mid = 0
        mid_one = 0
        if len(sort) <= 1:
            return sort[0]
        if len(sort) % 2 == 0:
            mid = sort[(len(sort)//2 - 1)]
            mid_one = sort[(len(sort)//2)]
            return (mid+mid_one)/2
        else:
            return sort[len(sort)//2]


        