from collections import Counter
from typing import List



def leastInterval(self, tasks: List[str], n: int) -> int:
    cnt = Counter(tasks)
    x = max(cnt.values)
    s = 0
    for k, v in cnt.items():
        if v == x:
            s += 1
    
    return max((x-1) * (n+1) + s, len(tasks))


