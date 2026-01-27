
class DoubleLinkNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = DoubleLinkNode(0, 0)
        self.tail = DoubleLinkNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hm = {} # key:node
        self.count = 0

    def __insert_to_front(self, node):
        # insert to front
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def __move_to_front(self, node):
        if self.head.next == node:
            return
        # remove from current position
        node.prev.next = node.next
        node.next.prev = node.prev

        self.__insert_to_front(node)

        pass

    def get(self, key: int) -> int:
        if key in self.hm:
            node = self.hm[key]
            self.__move_to_front(node)
            return node.val
        return -1
    
    def __remove_last(self):
        # self.print()
        if self.tail.prev != self.head:
            node = self.tail.prev

            self.tail.prev = node.prev
            self.tail.prev.next = self.tail

            node.prev = None
            node.next = None
            del self.hm[node.key]

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            node = self.hm[key]
            node.val = value
            self.__move_to_front(node)
            return
        
        node = DoubleLinkNode(key, value)
        self.hm[key] = node
        if self.count == self.capacity:
            self.__remove_last()
            self.count -= 1
        
        self.__insert_to_front(node)
        self.count += 1
    
    # def print(self):
    #     node = self.head.next
    #     print("-----")
    #     while node != self.tail:
    #         print(node.key, node.val)
    #         node = node.next

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

lRUCache = LRUCache(2)
lRUCache.put(1, 1) # cache is {1=1}

lRUCache.put(2, 2) # cache is {1=1, 2=2}
# lRUCache.print()
print(lRUCache.get(1))    # return 1
# lRUCache.print()
lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.print()
print(lRUCache.get(2))    # returns -1 (not found)
lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.print()
print(lRUCache.get(1))    # return -1 (not found)
print(lRUCache.get(3))    # return 3
lRUCache.print()
print(lRUCache.get(4))    # return 4
lRUCache.print()