# 146 LRU Cache
# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
# The cache is initialized with a positive capacity.
# Follow up:
# Could you do both operations in O(1) time complexity?
# Example:
# LRUCache cache = new LRUCache( 2 /* capacity */ );
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4      
# https://leetcode.com/problems/lru-cache/discuss/45912/Python-O(1)-solution-with-dummy-head-and-tail
# https://leetcode.com/problems/lru-cache/discuss/45952/Python-concise-solution-with-dummy-head-and-tail
# https://leetcode.com/problems/lru-cache/discuss/45946/Python-concise-solution 
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head # double linked list
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return node.val        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            node = self.head.next
            self._remove(node)
            del self.cache[node.key]
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
param_1 = obj.get(1)
obj.put(3, 3)
param_2 = obj.get(2)
obj.put(4, 4)
param_3 = obj.get(1)
param_4 = obj.get(3)
param_5 = obj.get(4)