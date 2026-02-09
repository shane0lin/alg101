from typing import List
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    groups = {}
    for str in strs:
        key = ''.join(sorted(str))
        if key not in groups:
            groups[key] = []
        groups[key].append(str)
    rst = []
    for k, v in groups.items():
        rst.append(v)
    return rst