# def coin_change(coins, target_amount):
# 	return -1

def coin_change(coins, target_amount):
    # Initialize DP array with infinity
    dp = [float('inf')] * (target_amount + 1)
    dp[0] = 0  # Base case

    for coin in coins:
        for amount in range(coin, target_amount + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[target_amount] if dp[target_amount] != float('inf') else -1
