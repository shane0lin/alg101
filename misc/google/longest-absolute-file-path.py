# 388. Longest Absolute File Path
# https://leetcode.com/problems/longest-absolute-file-path/
def lengthLongestPath(self, input: str) -> int:
    stack = []
    max_len = 0
    for line in input.split('\n'):
        print(line)
        depth = line.count('\t')
        print("depth: ", depth)
        while len(stack) > depth:
            stack.pop()
        if '.' in line:
            max_len = max(max_len, len('/'.join(stack)) + len(line) - depth)
        else:
            stack.append(line.replace('\t', ''))
    return max_len

# print(lengthLongestPath("", "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")) # 20
print(lengthLongestPath("", "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")) # 32