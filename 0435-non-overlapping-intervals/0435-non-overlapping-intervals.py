class Solution(object):
    def eraseOverlapIntervals(self, nums):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        nums.sort(key=lambda x:x[0])
        count=0 
        print(nums)

        prev = nums[0] #1,2
        for i in range(1,len(nums)): 
            if prev[1]>nums[i][0] : #means overlapping 
                count+=1 
                prev[1]=min(prev[1],nums[i][1])
            else: 
                prev[1]= nums[i][1]
            
        return count
            
        