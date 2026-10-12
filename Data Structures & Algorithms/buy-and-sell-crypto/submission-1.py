class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPrice = prices[0]
        maxProfit = 0

        for val in prices:
            profit = val - minPrice
            
            maxProfit = max(profit, maxProfit)
            minPrice = min(val, minPrice)
        return maxProfit