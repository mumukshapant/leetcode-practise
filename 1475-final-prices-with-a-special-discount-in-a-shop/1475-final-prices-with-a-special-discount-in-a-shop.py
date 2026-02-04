class Solution(object):
    def finalPrices(self, nums):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        # Time : O(n2)
        i=0
        j=1
        n= len(nums)
        res=nums[:]

        for i in range(n): 
            for j in range(i+1, n): 
                if nums[j]<=nums[i]: 
                    res[i] = nums[i]-nums[j]
                    break 
        return res

        