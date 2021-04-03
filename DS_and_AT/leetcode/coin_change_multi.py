def coinChange(coins, amount: int) -> int:

    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins: # 2 
        for x in range(coin, amount + 1): #2..6
            dp[x] = min(dp[x], dp[x-coin] + 1)
            
    return dp[amount] if dp[amount] != float('inf') else -1

print(coinChange([1,2,3], 6))

