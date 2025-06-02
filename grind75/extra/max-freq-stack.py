# 895 Maximum Frequency Stack
class FreqStack:
    def __init__(self):
        self.freq = {} # num: freq
        self.freqstack = {} # freq: list
        
        self.maxfreq = 0

    def push(self, x: int) -> None:
        if not x in self.freq:
            self.freq[x] = 0
        self.freq[x] += 1

        curStack = self.freqstack.get(self.freq[x], [])
        curStack.append(x)
        
        self.maxfreq = max(self.maxfreq, self.freq[x])
        self.freqstack[self.freq[x]] = curStack

    def pop(self) -> int:
        x = self.freqstack[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.freqstack[self.maxfreq]:
            self.maxfreq -= 1
        return x

FreqStack = FreqStack()
FreqStack.push(5)
FreqStack.push(7)
FreqStack.push(5)
FreqStack.push(7)
FreqStack.push(4)
FreqStack.push(5)
print(FreqStack.pop()) # 5
print(FreqStack.pop()) # 7
print(FreqStack.pop()) # 5
print(FreqStack.pop()) # 4
print(FreqStack.pop()) # 7
print(FreqStack.pop()) # 5