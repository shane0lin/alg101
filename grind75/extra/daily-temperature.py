# 739. Daily Temperatures
# Medium
# 3059
# 96    
# Add to List
# Share
# Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
# Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
def dailyTemperatures(T):
    stack = []
    res = [0] * len(T)
    for i in range(len(T)):
        while stack and T[stack[-1]] < T[i]:
            res[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)
    return res
print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(dailyTemperatures([30,60,90]))
print(dailyTemperatures([30,60,90,60,90,100,60]))
print(dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))