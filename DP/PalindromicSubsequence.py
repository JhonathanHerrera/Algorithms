
'''

Give a string 'S', find the length of the Longest Palidromic Subsequence in it.


Memoization Matrix steps

1) 2 + Diangonally previous cell
2) Max of Cells
3) Mark all Diagonal cells as 1 and below diagonal as 0
4) Diagonal Order

See Matrix in this video:
https://www.youtube.com/watch?v=yZWmS6CXbQc

Pseudocode

1) Declare all Diagonal cells of matrix as 1
2)

For each cell above diagonal
if str[i] == str[j]
	matrix[i][j] = 2 + matrix[i+1][j-1]
else
	matrix[i][j] = max(matrix[i+1][j], matrix[i][j-1] 
'''

#Recursive


s = "LEETCODE"
lo = 0
hi = len(s)-1

def lps(s, lo, hi):
	
	#Base case 1: If there is only 1 char
	if lo == hi:
		return 1
	
	#Base case 2: If there are 2 char and both are the same
	if s[lo] == s[hi] and lo+1 == hi:
		return 2
	
	#If ther first and last char match
	if s[lo] == s[hi]:
		return lps(s, lo+1, hi-1)

	#If the first and last char do not match
	return max(lps(s,lo,hi-1), lps(s,lo+1,hi))

#Recursive with memo

def lps(s, lo, hi, memo):
	if (lo, hi) in memo:
		return[(lo,hi)]
	if lo == hi:
		return 1
	
	if s[lo] == s[hi] and lo + 1 == hi:
		return 2
	if s[lo] == s[hi]:
		return memo[(lo,hi)] = lps(s,lo+1,hi-1,memo)
		
	return max[(lo,hi)] = max(lps(s,lo+1,hi,memo),
				  lps(s,lo, hi-1,memo)) 

#2D Table

def lps(s):
	n = len(s)

	#Step 1: Create a DP table and initialize it with 0s
	dp = [[0]*n for _ in range(n)]

	#Step 2: All diagonal cells are set to 1 (single-character palindromes)
	for i in range(n):
		dp[i][i] = 1

	#Step 3: Fill the DP table for substrings of increasing length
	for length in range(2, n+1): #length of the substring
		for i in range(n-length+1): #start index of the substring
			j = i + length - 1 #end index of the substring
			if s[i] == s[j]:
				dp[i][j] = 2 + dp[i+1][j-1] #expand around the matching pair
			else:
				dp[i][j] = max(dp[i+1][j], dp[i][j-1]) # take the best option
	#Step 4: Return the value in the top-right corner of the DP Table
	return dp[0][n-1]	
 
