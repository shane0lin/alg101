from collections import Counter


def subarraySum(nums: list[int], k: int) -> int:
    cnt = Counter({0:1})
    s = 0
    rst = 0
    for num in nums:
        s += num
        rst += cnt[s-k]
        cnt[s] += 1
        print(cnt)
    
    return rst


# print(subarraySum(nums = [1,1,1], k = 2))
print(subarraySum(nums = [1,2,3], k = 3))