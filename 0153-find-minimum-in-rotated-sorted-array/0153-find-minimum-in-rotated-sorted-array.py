class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n= len(nums)
        lo,hi=0,n-1

        minleft=float('-inf')
        minright= float('-inf')

        while lo<hi : 
            mid= lo+(hi-lo)//2

            # if nums[lo]> nums[mid]
            # min is either nums[mid] or nums[hi]

            # if nums[lo]<nums[mid] and nums[hi] < nums[mid]
            # min is nums[hi]
            if nums[mid]>nums[hi]: 
                lo=mid+1
            else:
                hi= mid
        
        return nums[lo]