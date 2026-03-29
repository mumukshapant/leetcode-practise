class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        """
        :type n: int
        :type meetings: List[List[int]]
        :type firstPerson: int
        :rtype: List[int]
        """
        meetings.sort(key= lambda x:x[2])
        res= {0,firstPerson} # people who know secret initially 
        i=0 
        total_meetings = len(meetings)

        while i<total_meetings : 
            currtime = meetings[i][2]

            graph = defaultdict(list) # temp graph for all meetings at curr time 
            people_in_currtime = set() 

            while i< total_meetings and meetings[i][2]==currtime: 
                x,y, _ = meetings[i]
                graph[x].append(y)
                graph[y].append(x)

                people_in_currtime.add(x)
                people_in_currtime.add(y)

                i+=1 # move to next meeting 
            # start BFS 
            q=deque() 
            visited =set() 
            for p in people_in_currtime: 
                if p in res: 
                    q.append(p)
                    visited.add(p)
            
            while q: 
                p = q.popleft() 
                for nei in graph[p]: 
                    if nei not in visited: 
                        visited.add(nei)
                        q.append(nei)
            res.update(visited)
        return list(res)