class Solution(object):
    def trap(self, nums):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(nums)
        left=0
        right= n-1 
        leftmax,rightmax=nums[0], nums[n-1]
        area=0 

        while left<right: 
            if leftmax<rightmax: 
                left+=1
                leftmax = max(nums[left], leftmax)
                area += leftmax - nums[left]
            else: 
                right-=1
                rightmax = max(nums[right], rightmax)
                area += rightmax - nums[right]
        return area 