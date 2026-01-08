class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Time : O(n), space O(n)
        res=set() 
        for i in nums: 
            if i in res: 
                return True
            else: 
                res.add(i)
        return False
        