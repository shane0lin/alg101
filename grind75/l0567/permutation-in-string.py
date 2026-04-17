from collections import Counter


def checkInclusion(s1: str, s2: str) -> bool:
    cnt = Counter(s1)
    required = len(cnt)
    m= len(s1)
    for i, ch in enumerate(s2):
        cnt[ch] -= 1
        if cnt[ch] == 0:
            required -= 1
        if i >= m:
            prev = s2[i-m]
            cnt[prev] += 1
            if cnt[prev] == 1:
                required += 1
        if required == 0:
            return True
    return False