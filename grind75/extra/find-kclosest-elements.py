# 658 Find K Closest Elements
def findClosestElements(arr, k, x):
    # left, right = 0, len(arr) - k
    # while left < right:
    #     mid = (left + right) // 2
    #     if x - arr[mid] > arr[mid + k] - x:
    #         left = mid + 1
    #     else:
    #         right = mid
    # return arr[left:left + k]
    

    # sol2
    import bisect
    right = left = bisect.bisect_left(arr, x) # find the index of the first element that is greater than or equal to x
    while right - left < k:
        # invariant: the range [left, right) has k elements
        if left == 0: return arr[:k]
        if right == len(arr): return arr[-k:]
        if x - arr[left - 1] <= arr[right] - x: left -= 1
        else: right += 1
    return arr[left:right]
    
print(findClosestElements([1,2,3,4,5], 4, 3)) # [1,2,3,4]
print(findClosestElements([1,2,3,4,5], 4, -1)) # [1,2,3,4]
print(findClosestElements([1,2,3,4,5], 4, 6)) # [2,3,4,5]
print(findClosestElements([1,2,3,4,5], 4, 2)) 