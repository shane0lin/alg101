def sortColors(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if not nums:
        return
    left, right = 0, len(nums) - 1 # left: first non-0; right: first non-2
    i = 0


    while i <= right:
        if nums[i]==0:
           nums[left], nums[i] = nums[i], nums[left]
           i += 1
           left += 1
        elif nums[i] == 2:
           nums[right], nums[i] = nums[i], nums[right]
           right -= 1
        else:
            i += 1

           
            