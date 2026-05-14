class Solution(object):
    def searchInsert(self, nums, t):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo=0
        hi= len(nums)-1

        while lo<=hi: 
            mid = lo+(hi-lo)//2
            if t==nums[mid] : 
                return mid
            elif t<nums[mid]: 
                hi=mid-1 
            else: 
                lo = mid+1
        return lo 


