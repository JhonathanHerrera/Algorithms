
'''

Unbounded knapsack problem:

We have n items, each one of them has a value vi and a weight wi, and we want to determine which items to take without exceeding the maximum weight k while having a total value that is as big as possible, you are asked to return their total value. We can take the same time more than once

'''

def knapSack(values, weights, k, lookup=None):
	lookup = {}
	if k in lookup:
		return lookup[k]
	
	max_value = 0
	for i in range(len(values)):
		if weights[i] <= k:
			max_value = max(max_value, values[i]+knapSack(values, weights, k-weights[i], lookup))
	lookup[k] = max_value
	return lookup[k]

def main():
	values = [20,30,15,25,10]	
	weights = [6,13,5,10,3]
	k = 20
	result = knapSack(values, weights, k)
	print(f"The Result is: {result}")

if __name__ == "__main__":
	main()
