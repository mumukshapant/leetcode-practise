class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pq=[] 
        for n in nums: 
            heapq.heappush(pq,(-n)) #maxheap
        
        for i in range(k-1): 
            heapq.heappop(pq)
        
        
        return (-heapq.heappop(pq))
        