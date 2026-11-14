class Solution(object):
    def twoSum(self, nums, t):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map={} 
       

        for i in range(len(nums)):
            rem = t-nums[i] #7
            if rem in map: 
                return [i,map[rem]]
            else : 
                map[nums[i]]=i # map= 2
        return map
