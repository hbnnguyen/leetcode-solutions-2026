# Last updated: 2/7/2026, 3:02:39 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        buy = 0
4        sell = 1
5        maxP = 0
6
7        while sell < len(prices):
8            if prices[sell] > prices[buy]:
9                profit = prices[sell] - prices[buy]
10                maxP = max(profit, maxP)
11            else:
12                buy = sell
13            sell += 1
14        
15        return maxP