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
        if not node: 
            return None 
        
        vis={}
        
        def dfs(node): 
            if node in vis:
                return vis[node]
                
            new_clone = Node(node.val)
            vis[node] = new_clone

            for nei in node.neighbors:
                new_clone.neighbors.append(dfs(nei))
            
            return new_clone
        return dfs(node)



        