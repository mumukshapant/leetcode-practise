class Solution(object):
    def insert(self, nums, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        nums.append(newInterval)
        nums.sort(key= lambda x : x[0])
        print(nums)

        #now add merge interval code 
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
