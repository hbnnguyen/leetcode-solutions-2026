# Last updated: 2/15/2026, 1:49:25 PM
1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3        dupes = set()
4
5        for n in nums:
6            if n in dupes:
7                return n
8            else:
9                dupes.add(n)
10        
11        