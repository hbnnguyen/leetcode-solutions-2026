# Last updated: 2/7/2026, 3:17:43 PM
1class Solution:
2    def checkInclusion(self, s1: str, s2: str) -> bool:
3        s1Dict = {}
4        for c in s1:
5            if c in s1Dict:
6                s1Dict[c] += 1
7            else:
8                s1Dict[c] = 1
9
10        l = 0
11        r = l + len(s1) - 1
12
13        while r < len(s2):
14            i = l
15
16            count = {}
17
18            while i <= r:
19                if s2[i] in s1Dict:
20                    if s2[i] in count:
21                        count[s2[i]] += 1
22                    else:
23                        count[s2[i]] = 1
24                
25                i += 1
26                
27                if count == s1Dict:
28                    return True
29
30            l += 1
31            r += 1
32        
33        return False
34        