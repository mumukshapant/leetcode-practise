class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        n = len(isConnected)
          
        # adj = defaultdict(list)
        # for i in range(n):
        #     for j in range(n): 
        #         if  isConnected[i][j]==1: 
        #             adj[i].append(j)
        count= 0
        vis=set()

        def dfs(node): 

            vis.add(node)
            # for nei in adj[node]: 
            for i in range(n):
                if isConnected[node][i] == 1 and i not in vis:
                    dfs(i)
            
        for i in range(n): 
            if i not in vis: 
                count+=1
                dfs(i)

        return count 



        