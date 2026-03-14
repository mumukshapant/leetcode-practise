class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n= len(nums)
        maxsum=float('-inf')
        maxlen = 0
        currsum=0 

#O(n) Time, O(1) space-- Optimal 

        for i in nums: 
            currsum+=i 

            maxsum= max(currsum, maxsum )

            if currsum<0 : 
                currsum=0 
        
        return maxsum
