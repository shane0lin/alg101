# 844. Backspace String Compare
# Easy
# 2599
# 125
def backspaceCompare(self, S: str, T: str) -> bool:
    def build(S):
        ans = []
        for c in S:
            if c != '#':
                ans.append(c)
            elif ans:
                ans.pop()
        return "".join(ans)
    return build(S) == build(T)