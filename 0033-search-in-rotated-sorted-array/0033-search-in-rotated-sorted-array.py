class Solution(object):
    def search(self, nums, t):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low=0
        high = len(nums)-1
        mid=0

        while low<=high : 
            mid=low+(high-low)/2
            print(mid)
            if nums[mid]==t: 
                return mid 

            elif nums[low]<=nums[mid]: 
                if t>=nums[low] and t<nums[mid]: 
                    high = mid-1
                else: 
                    low = mid+1 

            else:
                if t>nums[mid] and t<=nums[high]: 
                    low=mid+1
                else: 
                    high = mid-1 
         

        return -1 
