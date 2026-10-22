class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n= len(isConnected)
        vis=set() 
        count=0 

        def dfs(node) : 
            vis.add(node)

            for i in range(n): 
                # for nei in isConnected: 

                    if i not in vis and isConnected[node][i]==1 : 
                        dfs(i)
        
        for i in range(n): 
            if i not in vis:
                count+=1 
                dfs(i)
        return count

