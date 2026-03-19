class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums = [1] + nums + [1]
        
        n = len(nums)
        dp=[[0]*n for i in range(n)]
        

        for l in range(1,n-1): # diagonally
            for i in range(1,n-l):  # across the diagonal
                j = i+l-1
                for k in range(i, j+1):  # deciding which balloon to burst the last 

                    left = 0 if i==k else dp[i][k-1]
                    right = 0 if j==k else dp[k+1][j]

                    left_val = nums[i-1]
                    right_val = nums[j+1]
                    
                    val = left_val * nums[k] * right_val

                    dp[i][j] = max(val+left+right, dp[i][j] )

        return dp[1][n-2]
