

def search(nums: list[int], target: int) -> int:
    start, end = 0, len(nums) - 1
    
    while start + 1 < end:
        mid = start + int((end-start)/2)
        print(start, mid, end)
    
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[start]:
            if nums[start] <= target <= nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[mid] <= target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
            
    if nums[start] == target:
        return start
    elif nums[end] == target:
        return end
    else:
        return -1
                    



# print(search(nums = [4,5,6,7,0,1,2], target = 0))
# print(search(nums = [3,5,1], target = 3))
print(search(nums = [4,5,6,7,8,1,2,3], target = 8))

