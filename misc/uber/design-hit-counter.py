# 362 Design a hit counter
# 在本题中，你需要设计一个敲击计数器类。

# 在该类中，存在以下几个函数：

# HitCounter()：无参构造函数
# void hit(int timestamp)：表示在指定时间发生一次敲击
# int getHits(int timestamp)：返回指定时间前 300 秒之内的总敲击数
# 其中 timestamp 为秒单位

class HitCounter:
    def __init__(self):
        self.hits = []
    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)
    def getHits(self, timestamp: int) -> int:
        # Remove hits that are outside the 300-second window
        while self.hits and self.hits[0] <= timestamp - 300:
            self.hits.pop(0)
        return len(self.hits)