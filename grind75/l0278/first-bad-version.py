

def isBadVersion(x: int):
    if x < 4:
        return False
    return True

def firstBadVersion(n: int) -> int:
    start, end = 1, n
    while start + 1 < end:
        mid = start + int((end - start) / 2)
        if isBadVersion(mid):
            end = mid
        else:
            start = mid + 1
    
    if isBadVersion(start):
        return start
    elif isBadVersion(end):
        return end
    else:
        return -1