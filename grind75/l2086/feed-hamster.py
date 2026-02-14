def minimumBuckets(hamsters: str) -> int:
    rst = 0
    i, n = 0, len(hamsters)

    while i < n:
        if hamsters[i] == 'H':
            if i+1 < n and hamsters[i + 1] == '.':
                rst += 1
                i += 2
            elif i >0 and hamsters[i-1] == '.':
                rst += 1
            else:
                return -1


        i += 1
    
    return rst

