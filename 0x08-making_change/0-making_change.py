#!/usr/bin/python3
"""
Coin Change Problem
"""

def makeChange(coins, total):
    """Determine the fewest number of coins to meet a given a total"""
    if total <= 0:
        return 0  # No coins needed if total is 0 or less

    # Create a dp array initialized to infinity
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for total of 0

    # Update dp array for each coin
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, return -1
    return dp[total] if dp[total] != float('inf') else -1
