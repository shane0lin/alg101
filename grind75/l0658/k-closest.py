from typing import List
from heapq import heappop, heappush


def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    # hp = []
    # for num in arr:
    #     heappush(hp, (-abs(num-x), num))
    #     if len(hp) > k:
    #         heappop(hp)
    
    # rst = []
    # while hp:
    #     dis, num = hp.pop()
    #     rst.append(num)
    
    # return rst
    arr.sort(key=lambda v: abs(v-x))
    return sorted(arr[:k])


print(findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3)) # Output: [1,2,3,4]