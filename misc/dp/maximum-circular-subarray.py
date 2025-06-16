# 918 
# Circular array version of #53
from functools import cache
def max_subarray_sum(arr: list[int], k: int) -> int:
    
    
    n = len(arr)
    
    @cache
    def dp(i, signal):
        if i == 0:
            return arr[i] * signal
        return arr[i] * signal + max(0, dp(i - 1, signal))
    

    max_orin = max(dp(i, 1) for i in range(n))
    max_rev = max(dp(i, -1) for i in range(n))
    
    return max_orin if max_orin < 0 else max(max_orin, max_rev + sum(arr))