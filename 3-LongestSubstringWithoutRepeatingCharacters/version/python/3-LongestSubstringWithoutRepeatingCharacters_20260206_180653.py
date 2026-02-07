# Last updated: 2/6/2026, 6:06:53 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        mp = {}
4        l = 0
5        res = 0
6
7        for r in range(len(s)):
8            if s[r] in mp:
9                l = max(mp[s[r]] + 1, l)
10            mp[s[r]] = r
11            res = max(res, r - l + 1)
12        return res