



#Coin Change with Unbound and Recursive Solution

def coinChange(self, coins, amount):
	
	def knapSack(coins, amount, lookup):
		if amount == 0:
			return 0
		if amount < 0:
			return float('inf')
		
		if amount in lookup:
			return lookup[amount]

		min_coin == float('inf')
		for coin in coins:
			result = knapSack(coins, amount-coin, lookup)
			if result != float('inf'):
				min_coin = min(min_coin, 1 + result)
		
		lookup[amount] = min_coins
		return lookup[amount]
	
	lookup = {}
	result = knapSack(coins, amount, lookup)
	return result if result != float('inf') else -1

#Coin Change with Unbound and Iterative Solution

def coinChange(self, coins, amount):
	
	dp = [float('inf') for _ in range(amounnt+1)]
	dp[0] = 0

	for index in range(1,amount+1):
		#For 1 coin, how many coins can I use
		for coin in coins:
			if index - coin >= 0:
				dp[index] = min(dp[index], dp[index-coin] + 1)
	return dp[-1] if dp[-1] != float('inf') else -1
