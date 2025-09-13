def coinChange(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return -1 if dp[amount] == amount + 1 else dp[amount]

coins = [1, 2, 5]
amount = 11
# coins = [2]
# amount = 3
# coins = [1]
# amount = 0
print(coinChange(coins, amount))


