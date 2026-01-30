
def singleNumber(self, nums: list[int]) -> int:
    rst = 0
    for num in nums:
        rst = rst ^ num

    return rst