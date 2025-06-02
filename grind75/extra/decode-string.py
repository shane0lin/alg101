# 394. Decode String
# https://leetcode.com/problems/decode-string/
def decodeString(self, s: str) -> str:
    stack = []
    for c in s:
        if c == ']':
            temp = ''
            while stack[-1] != '[':
                temp = stack.pop() + temp
            stack.pop()
            num = ''
            while stack and stack[-1].isdigit():
                num = stack.pop() + num
            stack.append(int(num) * temp)
        else:
            stack.append(c)
    return ''.join(stack)

print(decodeString("", "3[a]2[bc]")) # "aaabcbc"
print(decodeString("", "3[a2[c]]")) # "accaccacc"
print(decodeString("", "2[abc]3[cd]ef")) # "abcabccdcdcdef"
# print( 5 * 'z')
# print('z' * 5)