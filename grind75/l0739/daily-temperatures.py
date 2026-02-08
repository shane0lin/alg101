
def dailyTemperatures(temperatures: list[int]) -> list[int]:
    
    n =len(temperatures)
    rst=[0] * n
    stack=[]


    for i in range(n): 
        temp = temperatures[i]
        while stack and temp > temperatures[stack[-1]]:
            prev_idx = stack.pop()
            rst[prev_idx] = i - prev_idx
        stack.append(i)
    return rst


print(dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73]))