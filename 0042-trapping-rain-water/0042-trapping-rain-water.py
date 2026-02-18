class Solution(object):
    def trap(self, nums):
        """
        :type height: List[int]
        :rtype: int
        """
        n= len(nums)
        left=[0]*n
        right=[0]*n

        left[0]= nums[0]
        right[n-1]=nums[n-1]
        
        area=0

        for i in range(1,n): 
            left[i]= max(nums[i],left[i-1])

        for i in range(n-2,-1,-1): 
            right[i]= max(right[i+1], nums[i])
        
        for i in range(0,n): 
            area+= min(left[i],right[i])-nums[i]
        
        return area
