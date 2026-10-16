class Solution(object):
    def numOfMinutes(self, n, headID, mgr, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        adj= defaultdict(list) # mgr : [employees]
        for index, manager in enumerate(mgr): 
            if manager ==-1 : 
                continue 
            adj[manager].append(index) # 2: [0,1,3,4,5]
        
        q = deque([(headID,0)])

        total_time=0 
        while q:
            curr_node, curr_time = q.popleft() 
            total_time = max(curr_time, total_time)

            for nei in adj[curr_node]: 
                q.append((nei, curr_time+informTime[curr_node]))
            
        return total_time
        