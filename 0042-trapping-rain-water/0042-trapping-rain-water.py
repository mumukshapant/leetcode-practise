class Solution(object):
    def trap(self, nums):
        """
        :type height: List[int]
        :rtype: int
        """
        n= len(nums)
        area=0 
        
        l,r=0,n-1

        leftptr , rightptr = nums[l], nums[r]

        while l<r: 
            if leftptr < rightptr : # jo chota hai, usko move karo 
                l+=1
                leftptr = max(nums[l] , leftptr)
                area += leftptr-nums[l]
                
            else: 
                r-=1
                rightptr =max(nums[r], rightptr)
                area+=rightptr - nums[r]
                
        return area



