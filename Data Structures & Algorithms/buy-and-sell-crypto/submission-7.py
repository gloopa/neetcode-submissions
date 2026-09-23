class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #iter through the prices list
        # buy -> minimum value within prices list
        # profit (sell - buy)!!  keep holding the max, then just return profit

        #[10, 1, 5, 6, 7, 1]
        # buy = 10, 1, 1, 1, 1, 1, 1 
        # profit = 0, 1 , 4, 5, 6, 0 
        #return 6!!! 

        buy = float('inf')
        profit = 0 
        
        for price in prices:
            buy = min(buy, price)
            profit = max(profit, price - buy)
        return profit
    

        