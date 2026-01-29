def missingNumber(self, nums: list[int]) -> int:
    n = len(nums)
    total = int(n*(n+1)/2)   
    actual = sum(nums)
    return total - actual