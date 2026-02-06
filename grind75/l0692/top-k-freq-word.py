from typing import List
from collections import Counter
from heapq import heappush, heappop, heapify


# def topKFrequent(words: List[str], k: int) -> List[str]:
    # hp = []
    # hm = {}
    # for word in words:
    #     if word not in hm:
    #         hm[word] = 1
    #     else:
    #         hm[word] +=1
    
    # for word, freq in hm.items():
    #     heappush(hp, (-freq, word))
    
    # rst = []
    # for _ in range(k):
    #     freq, word = heappop(hp)
    #     rst.append(word)
    # return rst


def topKFrequent(words: List[str], k: int) -> List[str]:
    freq = Counter(words)
    hp = [(-cnt, word) for word, cnt in freq.items()]
    heapify(hp)

    return [heappop(hp)[1] for _ in range(k)]
    
print(topKFrequent(words = ["i","love","leetcode","i","love","coding"], k = 2)) 
print(topKFrequent(words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4)) 