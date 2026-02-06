# Last updated: 2/5/2026, 10:04:14 PM
# bad attempt, try again
1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:
3        res = []
4        nums.sort()
5
6        for i, a in enumerate(nums):
7            if a > 0:
8                break
9
10            if i > 0 and a == nums[i - 1]:
11                continue
12
13            l, r = i + 1, len(nums) - 1
14            while l < r:
15                threeSum = a + nums[l] + nums[r]
16                if threeSum > 0:
17                    r -= 1
18                elif threeSum < 0:
19                    l += 1
20                else:
21                    res.append([a, nums[l], nums[r]])
22                    l += 1
23                    r -= 1
24                    while nums[l] == nums[l - 1] and l < r:
25                        l += 1
26
27        return res