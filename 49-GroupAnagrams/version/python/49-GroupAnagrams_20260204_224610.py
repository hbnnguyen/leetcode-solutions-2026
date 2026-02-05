# Last updated: 2/4/2026, 10:46:10 PM
# this was a bad attempt. try again
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        res = defaultdict(list)
4
5        for string in strs:
6            count = [0] * 26
7
8            for char in string:
9                count[ord(char) - ord('a')] += 1
10            
11            res[tuple(count)].append(string)
12        
13        return list(res.values())
14