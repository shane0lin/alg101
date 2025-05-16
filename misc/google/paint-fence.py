# 276 Paint Fence
# There is a fence with n posts, each post can be painted with one of the k colors.
# You have to paint all the posts such that no more than two adjacent fence posts have the same color.
# Return the total number of ways you can paint the fence.
# Note: n and k are non-negative integers.
# Example:
# Input: n = 3, k = 2
# Output: 6
# Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:
#             post1  post2  post3      
#      -----      -----  -----         
#        1         2      1
#        1         2      2
#        1         1      2
#        1         2      1
#        2         1      2
#        2         2      1
# Link: https://leetcode.com/problems/paint-fence/
def paintFence(n, k):
    if n == 0:
        return 0
    if n == 1:
        return k
    same = k
    diff = k * (k - 1)
    for i in range(3, n + 1):
        same, diff = diff, (same + diff) * (k - 1)
    return same + diff

# Another solution
def numWays(n, k):
    dp = [0, k, k * k]
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) * (k - 1)
    return dp[-1]


print(paintFence(3, 2)) # 6
print(paintFence(2, 2)) # 4