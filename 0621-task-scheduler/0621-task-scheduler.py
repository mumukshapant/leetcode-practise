class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq=Counter(tasks)
        pq=[-counts for counts in freq.values()] 
        heapq.heapify(pq)
        print(pq)

        time=0 
        q=deque() 

        while pq or q : 
            time+=1 

            if pq: 
                currel = 1+heapq.heappop(pq)
                if currel : 
                    q.append([currel, time+n])
            if q and q[0][1]==time: 
                heapq.heappush(pq, q.popleft()[0])
        return time 



        