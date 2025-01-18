
'''
72. Edit Distance

https://leetcode.com/problems/edit-distance/description/
https://www.youtube.com/watch?v=We3YDTzNXEk

def function
if str1[i] == str2[j]
	T[i][j] = T[i-1][j-1]
else
	T[i][j] = min(T[i-1][j],T[i][j-1],T[i-1][j-1])

'''

def minDistance(self, word1: str, word2: str) -> int:

        col,row = len(word1),len(word2)

        dp = [[0]*(1+col) for _ in range(row+1)]


        for i in range(col+1):
            dp[0][i] = i 
        
        for i in range(row+1):
            dp[i][0] = i 
        
        for i in range(1,row+1):
            for j in range(1,col+1):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                     dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        return dp[row][col]

