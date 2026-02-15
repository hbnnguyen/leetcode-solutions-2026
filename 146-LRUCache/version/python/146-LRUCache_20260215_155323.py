# Last updated: 2/15/2026, 3:53:23 PM
1class Node:
2    def __init__(self, key, val):
3        self.key, self.val = key, val
4        self.prev = self.next = None
5
6class LRUCache:
7    def __init__(self, capacity: int):
8        self.cap = capacity
9        self.cache = {}  # map key to node
10
11        self.left, self.right = Node(0, 0), Node(0, 0)
12        self.left.next, self.right.prev = self.right, self.left
13
14    def remove(self, node):
15        prev, nxt = node.prev, node.next
16        prev.next, nxt.prev = nxt, prev
17
18    def insert(self, node):
19        prev, nxt = self.right.prev, self.right
20        prev.next = nxt.prev = node
21        node.next, node.prev = nxt, prev
22
23    def get(self, key: int) -> int:
24        if key in self.cache:
25            self.remove(self.cache[key])
26            self.insert(self.cache[key])
27            return self.cache[key].val
28        return -1
29
30    def put(self, key: int, value: int) -> None:
31        if key in self.cache:
32            self.remove(self.cache[key])
33        self.cache[key] = Node(key, value)
34        self.insert(self.cache[key])
35
36        if len(self.cache) > self.cap:
37            lru = self.left.next
38            self.remove(lru)
39            del self.cache[lru.key]
40        
41
42
43# Your LRUCache object will be instantiated and called as such:
44# obj = LRUCache(capacity)
45# param_1 = obj.get(key)
46# obj.put(key,value)