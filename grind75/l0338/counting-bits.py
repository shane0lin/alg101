    """算法：动态规划(dp)
算法思路
当i为奇数，它比i-1在最低位上多1，其包含1的个数是i-1包含1的个数+1（i/2包含1的个数与i-1包含1的个数相同）

若i为偶数，其最低位上是0，包含1的个数为i右移一位包含1的个数，即为i/2包含1的个数

代码思路
dp[i]表示i包含1的个数

状态转移方程为dp[i] = dp[i / 2]+i % 2

复杂度分析
N表示要输出数组的长度，大小与num相等

空间复杂度：O(N)

时间复杂度：O(N)

    """
from typing import List


def countBits(self, n: int) -> List[int]:
    dp = [0] * (n+1)
    for i in range(1, n+1):
        dp[i] = dp[i>>1] + i%2
    return dp 
