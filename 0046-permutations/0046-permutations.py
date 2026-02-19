class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        #O(n!) --- please see note
        n = len(nums)
        curr,res=[],[]
        visited = [False] * n

        def backtrack(curr): 

            if len(curr)==len(nums): 
                res.append(curr[:])
                return res
            
            for i in range(len(nums)) :
                if not visited[i]:
                    visited[i]= True
                    curr.append(nums[i])
                    backtrack(curr)
                    curr.pop() 
                    visited[i]= False

        backtrack(curr)
        return res
        # # O(n*n!) 
        # n = len(nums)
        # curr,res=[],[]

        # def backtrack(curr): 

        #     if len(curr)==len(nums): 
        #         res.append(curr[:])
        #         return res
            
        #     for n in nums: 
        #         if n not in curr: 
        #             curr.append(n)
        #             backtrack(curr)
        #             curr.pop() 

        # backtrack(curr)
        # return res