class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n= len(nums)
        buckets = [[] for _ in range(n+1)]

        freq= Counter(nums)

        for el,fr in freq.items(): 
            buckets[fr].append(el)
        
        res=[] 

        for b in buckets[::-1]: 
            for num in b : 
                res.append(num)
                k-=1

                if k==0: 
                    return res 
        
