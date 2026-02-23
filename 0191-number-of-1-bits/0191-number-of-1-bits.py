class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=0 

        while n: 
            n= n&(n-1) # Update n = n & (n - 1) to remove the rightmost 1 bit
            res+=1

        return res 
        
        # NEETCODE 
        # Time : O(1), space O(1)