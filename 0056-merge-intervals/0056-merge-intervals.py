class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x:x[0]) # n*log n 

        curr=intervals[0]
        res=[]
        
        for i in range(1,len(intervals)): 
            
            if curr[1]>=intervals[i][0] : 
                #merge 
                curr[1]=max(curr[1],intervals[i][1]) # 1,6
                
            else: 
                res.append(curr)
                curr= intervals[i]
        res.append(curr)
        return res



        