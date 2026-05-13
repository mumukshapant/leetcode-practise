class Solution(object):
    def merge(self, nums):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        nums.sort(key=lambda x: x[0]) # O(n log n )
        prev = nums[0] # 1,3 
        res=[] 
       
        for i in range(1,len(nums)): 
            curr = nums[i] #2,6

            if prev[1]>=curr[0]: 
                # merge 
                prev[1]= max(curr[1], prev[1]) # 1,6
            else: 
                res.append(prev)
                prev= curr
        res.append(prev)
        return res

                
        

        