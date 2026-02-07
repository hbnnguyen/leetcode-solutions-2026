# Last updated: 2/6/2026, 6:07:19 PM
1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        count = {}
4        res = 0
5
6        l = 0
7        maxf = 0
8        for r in range(len(s)):
9            count[s[r]] = 1 + count.get(s[r], 0)
10            maxf = max(maxf, count[s[r]])
11
12            while (r - l + 1) - maxf > k:
13                count[s[l]] -= 1
14                l += 1
15            res = max(res, r - l + 1)
16
17        return res