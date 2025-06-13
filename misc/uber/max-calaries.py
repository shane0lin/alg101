# You have a specific budget, and your goal is to get the maximum amount of calories that can be bought

# with this budget.



# Input:

# A list of doubles representing the dollar prices of items (example: 1.25 for $1.25)

# A list of integers representing the calories value of each item in the same order as prices.

# A double representing your budget in dollar amount (example: 20.00 for $20)



# Output:

# An integer representing the maximum amount of calories that can be bought

# without going over the budget.

# To solve this problem, we can use a dynamic programming approach similar to the knapsack problem. Here's a step-by-step breakdown of the solution:
# 1. **Define the State**: Let `dp[i]` represent the maximum calories that can be obtained with a budget of `i` dollars.
# 2. **Initialize the State**: Initialize `dp[0]` to 0 because with a budget of 0 dollars, you can get 0 calories. For all other budgets, initialize `dp[i]` to a very small number (or negative infinity) to signify that those states are initially unreachable.
# 3. **State Transition**: For each item, update the `dp` array. If you can afford to buy the item (i.e., its price is less than or equal to the current budget), update the `dp` array to reflect the maximum calories you can get by either not buying the item or buying the item and adding its calories to the previous state.
# 4. **Result**: The result will be the maximum value in the `dp` array up to the given budget.
# Here's the implementation in Python:    

def max_calories(prices, calories, budget):
    # Convert budget to an integer to avoid floating-point precision issues
    budget = int(budget * 100)
    prices = [int(price * 100) for price in prices]
    # Initialize the dp array
    dp = [0] * (budget + 1)
    # Iterate over each item
    for price, calorie in zip(prices, calories):
        # Update the dp array from back to front to avoid overwriting
        for b in range(budget, price - 1, -1):
            dp[b] = max(dp[b], dp[b - price] + calorie)
    # The maximum calories that can be obtained with the given budget
    return dp[budget]
# Example usage
prices = [1.25, 2.00, 3.50]
calories = [100, 200, 300]
budget = 20.00
print(max_calories(prices, calories, budget))  # Output: 600