# Last updated: 2/6/2026, 6:03:12 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        maxP = 0
4        minBuy = prices[0]
5
6        for sell in prices:
7            maxP = max(maxP, sell - minBuy)
8            minBuy = min(minBuy, sell)
9        return maxP