from sys import maxsize
def maxProfit(prices: list[int]) -> int:
    curMin, profit = maxsize, 0
    for price in prices:
        if price < curMin:
            curMin = price
        if price - curMin > profit:
            profit = price - curMin
    return profit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))

