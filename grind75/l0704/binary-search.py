

def search(nums: list[int], target: int) -> int:
    if not nums:
        return -1
    
    start, end = 0, len(nums) - 1

    while start + 1 < end:
        mid = start + round((end - start) / 2)
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            start = mid
        else:
            end = mid
    
    if target == nums[end]:
        return end
    elif target == nums[start]:
        return start
    else:
        return -1 


print(search(nums = [-1,0,3,5,9,12], target = 9))
print(search(nums = [-1,0,3,5,9,12], target = 2))
