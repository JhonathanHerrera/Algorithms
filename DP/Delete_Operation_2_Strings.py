
'''
This is question 583 of Leetcode
https://leetcode.com/problems/delete-operation-for-two-strings/description/

This question can be rewrite as "How many letters each in both strings, and how many edits on both words needs to happen"

'''

#Solution one, 2D Graph

def minDistance_solution_1(word1, word2):	
	m, n = len(word1), len(word2)
	dp = [[0] * (n+1) for _ in range(m+1)]
	
	for i in range(1,m+1):
		for j in range(1,n+1):
			if word1[i-1] == word2[j-1]:
				dp[i][j] = 1 + dp[i-1][j-1]
			else:
				dp[i][j] = max(dp[i-1][j],dp[i][j-1])

	#(m−LCS Length)+(n−LCS Length)
        #m+n−2×LCS Length
	return m+n - 2 * dp[m][n]

#Solution two, Top-Down

def minDistance_solution_2(word1, word2):	
	
	m,n = len(word1),len(word2)
	
	@cache
	def lcs(i,j):
		if i == m or j == n:
			return 0	

		return 1 + lcs(i+1,j+1) if word1[i] == word2[j] else max(lcs(i+1,j),lcs(i,j+1))
	return m+n - 2*lcs(0,0)	
