class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        i = 0
        
        while i < len(prices):
            min_price=min(min_price,prices[i])
            max_profit=max(max_profit,prices[i]-min_price)
            i+=1
        return max_profit