class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        curr=[]
        res=[]

        def helper(i): 
            if i>=len(nums): 
                res.append(curr[:])
                return res

            curr.append(nums[i])
            helper(i+1)
            curr.pop()
            helper(i+1)
            
        helper(0)
        return res
    
    # TIME Complexity 
    '''
        2^n - for every element 2 choice: include or not include
        This needs to be done n times ( height = n) 

        time Complexity = n*2^n
    '''