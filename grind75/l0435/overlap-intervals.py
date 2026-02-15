def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    if not intervals:
        return 0

    rst = len(intervals)

    intervals.sort(key=lambda x: x[1])

    pre = -1
    for left, right in intervals:
        if left <= pre:
            rst -= 1
            pre = right
    return rst


