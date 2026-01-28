def containsDuplicate(nums: list[int]) -> bool:
    elements = set()
    for num in nums:
        if num in elements:
            return True
        elements.add(num)
    return False
