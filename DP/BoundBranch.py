
'''
Youtube video by Abdul that explains it will
https://www.youtube.com/watch?v=yV1d-b_NeK8

You can think about using Bound as "Take it (1) or not take it (0)"
And then you can solve the problem recursivley and draw it out as a branch as the one showed here
https://www.geeksforgeeks.org/0-1-knapsack-using-branch-and-bound/

Make sure to add base conditions
Also memo hash map !
'''

#1049. Last Stone Weight II

from typing import List
import collections

def Bound(stones: List[int]) -> int:
	totalSum = sum(stones)
	target = totalSum // 2
	def backTrack(i, total):
		if total >= target or i == len(stones):
			return abs(total-(totalSum - total))
		if (i, total) in dp:
			return dp[(i, total)]
		
		#Include or not include
		dp[(i, total)] = min(backTrack(i+1, total),
				backTrack(i+1, total + stones[i]))
		return dp[(i, total)]
	
	dp = collections.defaultdict(int)
	return backTrack(0,0)

def main():
	stones = [2,7,4,1,8,1]
	answer = 1
	result = Bound(stones)
	print(f"Expected Result: {answer} My Result: {result}")

if __name__ == "__main__":
	main()
