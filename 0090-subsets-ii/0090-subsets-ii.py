class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort() 

        
        def backtrack(curr, i ): 
            if i>=len(nums): 
                res.append(curr[:]) # : so that we append a shallow copy of the list  
                return res 
            
            curr.append(nums[i])
            backtrack(curr, i+1)
            curr.pop() 

            # Exclude nums[i] AND skip all duplicates -- chatgpt idea
            while i+1  <len(nums) and nums[i]==nums[i+1]: 
                i+=1
            backtrack(curr, i+1)       
        
        backtrack([], 0 )
        return res