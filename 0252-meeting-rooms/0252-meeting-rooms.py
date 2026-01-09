class Solution(object):
    def canAttendMeetings(self, nums):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not nums: 
            return True
        nums.sort(key=lambda x:x[0])

        prev= nums[0]
        for i in range(1, len(nums)): 
            if prev[1]<=nums[i][0]: 
                prev= nums[i]
            else: 
                return False

        return True
        