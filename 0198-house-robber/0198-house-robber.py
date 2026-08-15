class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==1 : 
            return nums[0]

        dp=[0]*n # Dp represents the max cost of robbing till that particular house 
        dp[0]=nums[0 ] # 2 
        dp[1]= max(nums[0], nums[1]) # 7 


        for i in range(2, n):
            dp[i] =  max(dp[i-2]+nums[i], dp[i-1])
        return dp[n-1]
