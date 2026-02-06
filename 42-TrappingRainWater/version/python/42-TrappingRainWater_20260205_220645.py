# Last updated: 2/5/2026, 10:06:45 PM
# bad attempt, try again
1class Solution:
2    def trap(self, height: List[int]) -> int:
3        if not height:
4            return 0
5
6        l, r = 0, len(height) - 1
7        leftMax, rightMax = height[l], height[r]
8        res = 0
9        while l < r:
10            if leftMax < rightMax:
11                l += 1
12                leftMax = max(leftMax, height[l])
13                res += leftMax - height[l]
14            else:
15                r -= 1
16                rightMax = max(rightMax, height[r])
17                res += rightMax - height[r]
18        return res