class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        dq= deque() 
        result =[] 

        for i in range(len(nums)):

            # i-k+1 ; any index<= (i-k+1) is out of the window 
            if dq and dq[0]<=i-k: 
                dq.popleft()

            # remove smaller values from back 
            while dq and nums[i]> nums[dq[-1]] : 
                dq.pop() 
            
            # Add the current index 
            dq.append(i)

            # once we have. processed k elements - the first window is ready 
            if i>=k-1 : 
                result.append(nums[dq[0]]) # front is the max value 

        return result 