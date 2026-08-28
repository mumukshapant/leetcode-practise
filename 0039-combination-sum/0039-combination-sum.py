class Solution(object):
    def combinationSum(self, nums, t):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]

        def backtrack(st, curr, currsum):
            if currsum==t:
                res.append(curr[:])
                return res
            
            if currsum>t: 
                return 
            
            for i in range(st, len(nums)): 
                
                currsum+=nums[i]
                curr.append(nums[i])
                backtrack(i, curr, currsum)
                curr.pop()
                currsum-=nums[i]

        backtrack(0, [], 0)
        return res