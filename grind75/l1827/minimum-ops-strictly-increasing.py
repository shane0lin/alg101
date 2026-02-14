def minOperations(nums: list[int]) -> int:
    ops = 0
    
    if not nums or len(nums) == 1:
        return ops

    cur_max = nums[0]
    for i in range(1, len(nums)):
        if nums[i] <= cur_max:
            ops += cur_max + 1 - nums[i]
            cur_max += 1
        else:
            cur_max = nums[i]

    return ops