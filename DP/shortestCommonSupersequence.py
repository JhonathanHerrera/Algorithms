

'''

Leetcode question 1092. Shortest Common Superseqeunce

Prereq: Do LCS first

'''

def shortestCommonSupersequence(string1, string2):	
	
	m,n = len(string1), len(string2)
	dp = [[0] * (n+1) for _ in range(m+1)]
	
	#Construct the LCS table
	for i in range(1,m+1):
		for j in range(1,n+1):
			if string1[i-1] == string2[j-1]:
				dp[i][j] = 1 + dp[i-1][j-1]
			else:
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])
	
	# Backtrack the LCS to construct the SCS
	i,j = m,n
	res = []
	
	while i > 0 or j > 0:
		if string1[i-1] == string2[j-1]:
			res.append(string1[i-1])
			i -=1
			j -=1
		elif dp[i-1][j] >= dp[i][j-1]: #Moves up the table
			res.append(string1[i-1])
			i -=1
		else: #Moves left in the table
			res.append(string2[j-1])
			j -=1
	#Add any remaining characters from either strings
	while i>0:
		res.append(strign1[i-1])
		i -=1

	while j>0:
                res.append(strign2[j-1])
                j -=1
	
	#The res will be reserve, so it needs to be undone
	res.reverse()
	return ''.join(res)		
