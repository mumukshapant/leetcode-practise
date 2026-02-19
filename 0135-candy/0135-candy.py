class Solution(object):
    def candy(self, nums):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n= len(nums)
        
        left = [1]*n
        for i in range(1,n):
            if nums[i-1] < nums[i]:
                left[i]= left[i-1]+1

        for i in range(n-2, -1, -1): 
            if nums[i+1] < nums[i]:
                left[i] = max(left[i],left[i+1]+1 )
        return sum(left)

