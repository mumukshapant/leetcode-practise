class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n= len(nums)
        curr,res=[],[]

        used=[False] * n  # used array 
        nums.sort()

        def backtrack(): 
            if len(curr)==n : 
                res.append(curr[:])
                return res
            
            for i in range(n):
                if used[i]: 
                    continue 
                
                if i>0 and nums[i]==nums[i-1] and not used[i-1]: 
                    continue

                curr.append(nums[i])
                used[i]= True 
                backtrack()
                curr.pop()
                used[i]= False

        backtrack()
        return res
