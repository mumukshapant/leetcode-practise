class Solution(object):
    def merge(self, nums):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        #sort in increasing order of first digit 
       
        res=[]
        prev= nums[0]

        for n in nums[1:] :
            if prev[1]>=n[0]: #merge
                prev[1] = max(prev[1],n[1]) # [1,6]
            else: 
                res.append(prev)
                prev=n

        res.append(prev)
        return res 