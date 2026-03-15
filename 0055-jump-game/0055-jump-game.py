class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n= len(nums)
        currpos =0 
        maxpos=0

        for i in range(n): 
            currpos =i 
            if currpos>maxpos: 
                return False
            maxpos = max(maxpos, currpos+nums[i]) 
            if maxpos>=n-1: 
                return True 
        return False
