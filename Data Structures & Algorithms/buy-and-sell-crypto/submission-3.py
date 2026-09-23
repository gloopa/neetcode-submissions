class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for sell in prices:
            buy = min(buy, sell)
            profit = max(profit, sell - buy)
        return profit 

        #o(N) since for loop up to N-1 values in list 
        # Space: o(1) since we are returning a variable
        