class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxP = 0

        for i in prices:
            maxP = max(maxP, i - minBuy)
            minBuy = min(minBuy, i)
        
        return maxP