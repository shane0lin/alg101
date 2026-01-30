def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return 
    if len(strs) == 1:
        return strs[0]
    
    index = 0
    minl = min(len(s) for s in strs)

    while index < minl:
        for i in range(1, len(strs)):
            if strs[i][index] != strs[i-1][index]:
                return strs[0][:index]
        index += 1
    return strs[0][:index]


print(longestCommonPrefix(strs=["cir","car"]))
print(longestCommonPrefix(strs=["ab","a"]))
print(longestCommonPrefix(strs=["flower","flow","flight"]))