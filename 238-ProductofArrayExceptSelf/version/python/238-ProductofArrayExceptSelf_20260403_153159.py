# Last updated: 4/3/2026, 3:31:59 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        
4        res = [1] * (len(nums))
5
6        prefix = 1
7        for i in range(len(nums)):
8            res[i] = prefix
9            prefix *= nums[i]
10
11        postfix = 1
12        for i in range(len(nums) -1, -1, -1):
13            res[i] *= postfix
14            postfix *= nums[i]
15        
16        return res