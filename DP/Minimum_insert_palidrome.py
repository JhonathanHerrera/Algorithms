

'''
1312. Minimum Insertion Steps to Make a String Palindrome

Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/description/

'''

def minInsertions(s):
	n = len(s)
	dp = [[0]*n for _ in range(n)]

	for i in range(n):
		dp[i][i] = 1

	for length in range(2,n+1):
		for i in range(n-length+1):
			for j = i+length-1
			if s[i] == s[j]:
				dp[i][j] = dp[i+1][j-1] + 2
			else:
				dp[i][j] = max(dp[i+1][j], 
                                    dp[i][j-1])
	return len(s) = dp[0][n-1]
