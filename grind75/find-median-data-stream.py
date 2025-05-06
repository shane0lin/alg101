# 295 Find Median from Data Stream
class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = [] # max heap
        self.large = [] # min heap
    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.small) < len(self.large):
            heapq.heappush(self.small, -heapq.heappop(self.large))
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0]) / 2.0
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()