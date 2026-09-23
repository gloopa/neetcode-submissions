class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        result = 0
        
        for i in range(1, len(prices)):
            buy = min(buy, prices[i])
            result = max(result, prices[i] - buy)
        
        return result
        
            