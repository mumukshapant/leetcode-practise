class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res=[-1]*n
        
        st=[]
        for i in range(2*n-1, -1, -1 ): 
            num = nums[i%n]

            while st and st[-1]<=num: 
                st.pop() 
            
            if st: 
                res[i%n]= st[-1]
            
            st.append(num)
        return res
        
        