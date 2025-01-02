
'''

The differences between Bound and UnBound KnapSacks using both recursive and iterative methods. 

NOTE:

In bounded knapsack, you cannot reuse values, so you need to keep track of the index placement and move it each time you decide to take an item. On the other hand, in unbounded knapsack, you can reuse values, meaning you don't need to move the index when deciding to take an item. Not moving the index while taking allows the value to be picked again in subsequent steps.

This distinction is more relevant to the recursive method, but a similar idea applies to the iterative approach (using a for loop). For bounded knapsack, you iterate over items while keeping track of whether they have been used. For unbounded knapsack, you iterate over the capacity while allowing the same item to be reused multiple times.

'''

def unbounded_knapsack_recursive(wt, val, W, n):
    if n == 0 or W == 0:
        return 0
    
    if wt[n - 1] <= W:
        return max(
            val[n - 1] + unbounded_knapsack_recursive(wt, val, W - wt[n - 1], n),  # Include item
            unbounded_knapsack_recursive(wt, val, W, n - 1)  # Exclude item
        )
    else:
        return unbounded_knapsack_recursive(wt, val, W, n - 1)

def unbounded_knapsack_iterative(wt, val, W):
    dp = [0] * (W + 1)

    for i in range(W + 1):
        for j in range(len(wt)):
            if wt[j] <= i:
                dp[i] = max(dp[i], dp[i - wt[j]] + val[j])
    
    return dp[W]


def bounded_knapsack_recursive(wt, val, W, n):
    if n == 0 or W == 0:
        return 0
    
    if wt[n - 1] <= W:
        return max(
            val[n - 1] + bounded_knapsack_recursive(wt, val, W - wt[n - 1], n - 1),  # Include item
            bounded_knapsack_recursive(wt, val, W, n - 1)  # Exclude item
        )
    else:
        return bounded_knapsack_recursive(wt, val, W, n - 1)

'''

MidPoint Note:
We can see that in bounded_knapsack_recursive that both calls has "n-1" while in unbounded_knapsack_recursive its both "n-1" and "n" being passed in

'''

#Likely chance you wont be a bounded iterative (recursive is a easier approach) but this is just for example comparison

def bounded_knapsack_iterative(wt, val, W):
    n = len(wt)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if wt[i - 1] <= j:
                dp[i][j] = max(
                    val[i - 1] + dp[i - 1][j - wt[i - 1]],  # Include item
                    dp[i - 1][j]  # Exclude item
                )
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[n][W]

def main():


	weights = [1, 3, 4]
	values = [10, 40, 50]
	capacity = 8

	Un_B = input("Do you want to see the Bounded or UnBounded approach?")
	R_I = input("Do you want it to be recursive or iterative?")
	
	if Un_B.lower() == "bounded":
		if R_I.lower() == "recursive":
			print(bounded_knapsack_recursive(weights, values, capacity, len(weights)))
		elif R_I.lower() == "iterative":
			 print(bounded_knapsack_iterative(weights, values, capacity))
		else:
			print("Pick a valid response")
	elif Un_B.lower() == "unbounded":
                if R_I.lower() == "recursive":
                        print(unbounded_knapsack_recursive(weights, values, capacity, len(weights)))
                elif R_I.lower() == "iterative":
                         print(unbounded_knapsack_iterative(weights, values, capacity))
                else:
                        print("Pick a valid response")	
	else:
		print("Pick a valid response")

if __name__ == "__main__":
	main()
