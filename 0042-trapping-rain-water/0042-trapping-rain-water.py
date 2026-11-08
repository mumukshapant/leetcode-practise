class Solution(object):
    def trap(self, nums):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(nums)
        l,r, lmax, rmax=0,n-1, nums[0], nums[n-1]

        area=0
        while l<r: 
            if lmax<rmax: 
                l+=1
                lmax=max(nums[l], lmax)
                area+=lmax-nums[l]
            else: 
                r-=1
                rmax=max(rmax, nums[r])
                area+=rmax-nums[r]
        
        return area 