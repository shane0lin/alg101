# LFU Cache
# https://leetcode.com/problems/lfu-cache/


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    # add to head
    def add(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def removeLast(self):
        if self.size == 0:
            return None
        last = self.tail.prev
        self.remove(last)
        return last
    

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.freq = {}
        self.minFreq = 0
    
    # update freq
    def update(self, node):
        freq = node.freq
        self.freq[freq].remove(node)
        if freq == self.minFreq and self.freq[freq].size == 0:
            self.minFreq += 1
        node.freq += 1
        if node.freq not in self.freq:
            self.freq[node.freq] = DoublyLinkedList()
        self.freq[node.freq].add(node)  

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.update(node)
        return node.val
    
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.update(node)
        else:
            if len(self.cache) == self.capacity:
                node = self.freq[self.minFreq].removeLast()
                del self.cache[node.key]
            node = Node(key, value)
            self.cache[key] = node
            if 1 not in self.freq:
                self.freq[1] = DoublyLinkedList()
            self.freq[1].add(node)
            self.minFreq = 1


# lru = LFUCache(3)
# lru.put(2, 2)
# lru.put(1, 1)
# print(lru.get(2)) # 2
# print(lru.get(1)) # 1
# print(lru.get(2)) # 2
# lru.put(3, 3)
# lru.put(4, 4)
# print(lru.get(3)) # -1
# print(lru.get(2)) # 2
# print(lru.get(1)) # 1
# print(lru.get(4)) # 4
lru = LFUCache(3)
lru.put(2, 2)
lru.put(1, 1)

lru.put(3, 3)
lru.get(3)
lru.put(4, 4)
lru.get(4)
lru.put(5, 5)
print(lru.get(5))
lru.put(6, 6)
print(lru.get(6))
lru.put(7, 7)
lru.put(8, 8)

print(lru.get(2)) # 2
print(lru.get(1)) # 1
