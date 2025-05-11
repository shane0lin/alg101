# 1235. Maximum Profit in Job Scheduling
from typing import List
import bisect
def jobScheduling(startTime, endTime, profit):
    # sol1
    # jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
    # dp = [[0, 0]] # dp[i] = [endTime, maxProfit]
    # for s, e, p in jobs:
    #     i = bisect.bisect(dp, [s + 1]) - 1
    #     if dp[i][1] + p > dp[-1][1]:
    #         dp.append([e, dp[i][1] + p])
    # return dp[-1][1]

    # sol2
    jobs = sorted(zip(endTime, startTime, profit))
    numJobs = len(jobs)
    dp = [0] * (numJobs + 1)
    
    for i, cur_end, cur_start, cur_profit in enumerate(jobs):
        index = bisect.bisect_right(jobs, cur_start, key=lambda v: v[0])
        dp[i + 1] = max(dp[i], dp[index] + cur_profit)
        

    return dp[numJobs]



print(jobScheduling([1,2,3,3], [3,4,5,6], [50,10,40,70]))
print(jobScheduling([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60]))
print(jobScheduling([1,1,1], [2,3,4], [5,6,4]))