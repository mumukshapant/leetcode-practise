class Solution(object):
    def combinationSum(self, nums, t):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        curr=[]
        res=[]
        
        def helper(i,currtotal):
            if i>=len(nums) or currtotal>t: 
                return 

            if currtotal==t: 
                res.append(curr[:])
                return res 

            curr.append(nums[i])
            helper(i,currtotal+nums[i])
            
            curr.pop()
            helper(i+1,currtotal)
        
        helper(0,0)
        return res

'''
In Subsets Question, we use  i+1 to include and i to exclude, whereas in this Q we use i to include and i+1 to exclude. WHY? 
In subsets, each element is allowed at most once.

So the moment you decide about nums[i] (include or exclude), you must move on to i + 1.
Staying at i would mean:   “I can reuse the same element again”

    Code snippet from Subsets: 
            curr.append(nums[i])
            helper(i+1)
            curr.pop()
            helper(i+1)


'''