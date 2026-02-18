class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        q=[]
        q.append((0,k)) #cost w1, source
        adj= defaultdict(list)

        for u,v,w in times: 
            adj[u].append((v,w))

        count=0 
        vis=set()

        while q:
            w1,n1 = heapq.heappop(q)

            if n1 in vis: 
                continue
            
            vis.add(n1)
            count= max(count,w1)

            
            for n2,w2 in adj[n1]: 
                if n2 not in vis: 
                    heapq.heappush(q, (w1+w2,n2))
                    

        return count if n==len(vis) else -1 


            