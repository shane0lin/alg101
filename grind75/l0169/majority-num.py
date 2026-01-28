def majorityElement(nums: list[int]) -> int:
    candidate, count = -1, 0
    for num in nums:
        if count == 0:
            candidate = num
        if candidate == num:
            count += 1
        else:
            count -= 1
    return candidate