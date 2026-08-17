class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        currsum=0 
        count=0 
        map={}
        map[0]=1

        for i in nums: 
            
            currsum+=i 
            if currsum-k in map: 
                count+=map.get(currsum-k)
            map[currsum]=map.get(currsum,0)+1
        return count