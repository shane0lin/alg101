package grind75.l0070;

public class ClimbStairs {
    public int climbStairs(int n) {
        if (n<=1) {
            return n;
        }
        int prev = 1, prev2 = 1;
        int cur = 0;
        for (int i=2; i<=n; i++) {
            cur = prev + prev2;
            prev2 = prev;
            prev = cur;
        }
        return cur;
    }

    public int climbStairs2(int n) {
        int[] dp = new int[n+1];
        dp[0] = 1;
        dp[1] = 1;
        for (int i = 2; i <=n; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        } 
        return dp[n];
    }
}
