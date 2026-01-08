class Solution(object):
    def insert(self, nums, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res=[] 
        for i in range(len(nums)): 
            #CASE 1 : 
            if newInterval[1] <nums[i][0] : 
                res.append(newInterval)
                return res+nums[i:]
            elif newInterval[0]> nums[i][1]: 
                res.append(nums[i])
            else: #merge
                newInterval = [
                    min(newInterval[0],nums[i][0]), 
                    max(newInterval[1], nums[i][1])
                    ]
        res.append(newInterval)
        return res


                   