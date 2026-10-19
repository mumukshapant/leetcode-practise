"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        st=[] 
        if not node: 
            return None
        
        vis={}

        def dfs(curr): 
            if curr in vis : 
                return vis[curr]
            
            clone = Node(curr.val)
            vis[curr]=clone

            #clone all nei 
            for nei in curr.neighbors: 
                nei_of_clone = dfs(nei)# Get the cloned neighbor
                clone.neighbors.append(nei_of_clone)#Connect it to the curr clone

            return clone 

        
        return dfs(node)

        