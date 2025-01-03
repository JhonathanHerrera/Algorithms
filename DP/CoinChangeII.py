

#This question can be down with 2 approaches.

#1 passed all cases on LC, the other didnt because of TME

#If seen during an interview, ask which approach you prefer and whether they are ok with it, even if it's not as optimal.

#Backtrack/Knapsack Unnbound (Preferred more)

#This solution is slow and beats 10%, but still passes the last test case 
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def backtrack(remaining: int, idx: int) -> int:
       
            if remaining == 0:
                return 1  
            if remaining < 0 or idx == len(coins):
                return 0  
            if (remaining, idx) in memo:
                return memo[(remaining, idx)]

            # Choices: take the coin or skip it
            include = backtrack(remaining - coins[idx], idx)  # Reuse the coin
            exclude = backtrack(remaining, idx + 1)  # Skip the coin

            # Memoize and return result
            memo[(remaining, idx)] = include + exclude
            return memo[(remaining, idx)]

        memo = {}
        return backtrack(amount, 0)

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def backtrack(remaining, start):
            # Base cases
            if remaining == 0:
                return 1 
            if remaining < 0:
                return 0  
            
            if (remaining, start) in memo:
                return memo[(remaining, start)]

            total_ways = 0
            for i in range(start, len(coins)):
                # Reuse the current coin by staying at index `i`
                total_ways += backtrack(remaining - coins[i], i)

            memo[(remaining, start)] = total_ways
            return total_ways
        memo = {}
        return backtrack(amount, 0)

#Bottom-Up Approach

def change(self, amount, coins):
	
	dp =[0 for _ in range(amount+1)]
	dp[0] = 1

	for coin in coins:
		for i in range(coin, amount + 1):
			dp[i] += dp[i-coin]
	return dp[amount]
