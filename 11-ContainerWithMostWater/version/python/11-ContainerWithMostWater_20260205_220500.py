# Last updated: 2/5/2026, 10:05:00 PM
# bad attempt, try again
1class Solution:
2    def maxArea(self, heights: List[int]) -> int:
3        l, r = 0, len(heights) - 1
4        res = 0
5
6        while l < r:
7            area = min(heights[l], heights[r]) * (r - l)
8            res = max(res, area)
9            if heights[l] <= heights[r]:
10                l += 1
11            else:
12                r -= 1
13        return res