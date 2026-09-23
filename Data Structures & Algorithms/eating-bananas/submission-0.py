class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 #min speed
        right = max(piles) #max speed possible
        result = right #holder

        def hours(speed):
            return sum(math.ceil(pile/speed) for pile in piles)

        while left <= right:
            k = (left + right) // 2
            hour = hours(k)
            if hour <= h:
                result = k
                right = k -1
            else:
                left = k+1
        return result




        