class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
    
        n= len(nums)
        bucket = [[] for _ in range(n+1)]
        
        map = Counter(nums)

        for el, freq in map.items(): 
            bucket[freq].append(el)
        
        
        res=[]

        for b in bucket[::-1]  :
            for num in b: 
                res.append(num)
                k-=1

                if k==0 : 
                    return res

    # Time :  O(n) Counter + O(n) iterating all elements 
    # Space : O(n) Counter +O(n) res