# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
def decodeString(s: str) -> str:
    num_s = []
    rst_s = []
    cur_num = 0
    rst = ''
    for ch in s:
        if ch.isdigit():
            cur_num = cur_num * 10 + int(ch)
        elif ch == '[':
            num_s.append(cur_num)
            rst_s.append(rst)
            cur_num = 0
            rst = ''
        elif ch == ']':
            rst = rst_s.pop() + rst * num_s.pop()
        else:
            rst += ch
    return rst

print(decodeString("100[abc]"))
        
