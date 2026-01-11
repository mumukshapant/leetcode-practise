class Solution(object):
    def minInterval(self, nums, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        nums.sort() 
#        heappq=[]
        res={} 
        i=0 
        arr =[] 

        for q in sorted(queries): 
            while i<len(nums) and q>=nums[i][0]: 
                l,r = nums[i]
                heapq.heappush(arr, (r-l+1,r))
                i+=1
            while arr and arr[0][1]<q: 
                heapq.heappop(arr)
            
            res[q] = arr[0][0] if arr else -1 
        return [res[q] for q in queries]
        



        