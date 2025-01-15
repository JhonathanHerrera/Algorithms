
'''
https://leetcode.com/problems/palindromic-substrings/description/
647. Palindromic Substrings

'''

def countSubstrings(s):
	n = len(s)
	dp = [[0] * n for _ in range(n)]

	res = 0
	for i in range(n):
		dp[i][i] = 1
		res += 1

	for i in range(n-1):
		if s[i] == s[i+1]:
			dp[i][i+1] = 1
			res += 1

	for length in range(3,n+1):
		 for i in range(n-length+1):
			j = i + length -1
			
			#The dp[i+1][j-1] is used to check if the s[i+1:j] is a subtring
			#Example: "abba" we see that s[0] and s[3] match (both are "a") but we need to also double check if s[1] and s[2] match
			#When dont they not match? In an example like this "abca". Thats why we do the dp[i+1][j-1] to make sure
			if s[i] == s[j] and dp[i+1][j-1]:
				dp[i][j] = 1
				res += 1

	return res 
