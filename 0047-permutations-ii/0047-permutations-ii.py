class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        visited= [False]*n 
        curr,res=[],[]
        nums.sort()

        def backtrack() : 
            if len(curr)==n: 
                res.append(curr[:])
                return res

            for i in range(n): 
                if visited[i]: 
                    continue

                if i<n-1 and nums[i]==nums[i+1] and not visited[i+1]: 
                    continue

                visited[i] = True
                curr.append(nums[i])
                backtrack()
                curr.pop() 
                visited[i] = False

        backtrack()
        return res


