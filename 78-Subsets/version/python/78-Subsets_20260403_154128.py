# Last updated: 4/3/2026, 3:41:28 PM
1class Solution:
2    def subsets(self, nums: List[int]) -> List[List[int]]:
3        res = []
4
5        subset = []
6        def dfs(i):
7            if i >= len(nums):
8                res.append(subset.copy())
9                return
10            
11            subset.append(nums[i])
12            dfs(i+1)
13
14            subset.pop()
15            dfs(i+1)
16
17        dfs(0)
18        return res