class Solution(object):
    def trap(self, nums):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(nums)
        l,r=0,n-1
        leftmax,rightmax=nums[l],nums[r]
        area=0


        while l<r: 
            
            if leftmax>rightmax: 
                r-=1
                rightmax= max(nums[r], rightmax)
                area+=rightmax- nums[r]
                
            else: 
                l+=1
                leftmax = max(nums[l], leftmax) 
                area+=leftmax-nums[l]
                
        
        return area
                

