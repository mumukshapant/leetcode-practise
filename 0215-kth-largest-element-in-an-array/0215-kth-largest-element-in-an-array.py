class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pq=[]
        if len(nums)==1 : 
            return nums[0]

        for i in range(k): 
            heapq.heappush(pq,nums[i])
        
        print(pq)
        
        for i in range(k, len(nums)): 
            element = pq[0]
            if nums[i] > element : 
                heapq.heappop(pq) 
                heapq.heappush(pq,nums[i])
        
        return pq[0]

