class Solution(object):
    def minMeetingRooms(self, nums):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        nums.sort(key=lambda x:x[0])

        count=0 
        start=[]
        end = [] 
        for i in range(len(nums)): 
            start.append(nums[i][0])
            end.append(nums[i][1])

        start.sort()
        end.sort() 
        res=0

        # start = [0,5,10]
        # end = [10,15,30]
        i,j=0,0
        while i< (len(nums)) and j <len(nums): 
            if start[i]<end[j]: 
                count+=1
                i+=1
            else: 
                count-=1
                j+=1

            res= max(count, res)


        return res

        