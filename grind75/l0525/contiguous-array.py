def findMaxLength(nums: List[int]) -> int:
    rst = 0
    prefix_hash = {0: -1}
    prefix_sum = 0
    for i, num in enumerate(nums):
        prefix_sum += 1 if num == 1 else -1
        if prefix_sum in prefix_hash: # we find a subarray that has equal 0s and 1s
            rst = max(rst, i-prefix_hash[prefix_sum])
        else:
            prefix_hash[prefix_sum] = i
    return rst


