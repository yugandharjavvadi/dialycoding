'''There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

Right, then down
Down, then right
Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

'''

def no_of_ways(m,n):
    dp=[[0 for i in range(m)]for j in range(n)]
    for i in range(n):
        dp[0][i]=1
    for j in range(m):
        dp[j][0]=1
    for i in range(1,n):
        for j in range(1,n):
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
    return dp[-1][-1]

print(no_of_ways(2,2))

print(no_of_ways(5,5)                )