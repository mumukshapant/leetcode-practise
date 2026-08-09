class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0 : 
            return 0 
        if n==1: 
            return 1
        if n==2 : 
            return 2

        dp = [0] * (n+1)
        dp[0]= 0 
        dp[1]= 1 
        dp[2]=2 
        for i in range(3, len(dp)): 
            dp[i] +=dp[i-2]+ dp[i-1]
        return dp[n]