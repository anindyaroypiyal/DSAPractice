
from sys import stdin

def lcs(text1, text2) :
	def memoization(i,j,dp):
		if i<0 or j<0:
			return 0

		if dp[i][j] != -1:
			return dp[i][j]

		if text1[i]==text2[j]:
			dp[i][j] = 1 + memoization(i-1,j-1,dp)
		else:
			dp[i][j] = max(memoization(i-1,j,dp), memoization(i,j-1,dp))
			
		return dp[i][j]
	
	def tabulation(n,m):
		dp = [ [0]*(m+1) for _ in range(n+1) ]
		
		for i in range(1,n+1):
			for j in range(1,m+1):
					if text1[i-1]==text2[j-1]:
						dp[i][j] = 1 + dp[i-1][j-1]
					else:
						dp[i][j] = max(dp[i-1][j], dp[i][j-1])
					
		return dp[n][m]

	
	n,m = len(text1),len(text2)

	# # For memoization
	# dp = [ [-1]*m for _ in range(n)]
	# return memoization(n-1,m-1,dp)

	# For tabulation
	return tabulation(n,m)




























    


#main
s = str(stdin.readline().rstrip())
t = str(stdin.readline().rstrip())

print(lcs(s, t))