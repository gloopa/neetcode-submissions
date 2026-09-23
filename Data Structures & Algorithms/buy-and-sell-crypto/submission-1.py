class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        min_buy = prices[0]
        profit = 0
        
        for price in prices:
            if price < min_buy:
                min_buy = price 
            else:
                profit = max(profit, price - min_buy)
        return profit

        

        