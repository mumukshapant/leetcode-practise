# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        
        
        def findparent(node,parent=None): 
            if not node: 
                return 
            node.parent= parent
            findparent(node.left, node)
            findparent(node.right, node)
        
        findparent(root)
        q=deque([(target, 0)]) #distance 
        vis={target}
        ans=[] 

        while q: 
            node,dis = q.popleft()
            
            if dis==k: 
                ans.append(node.val)
                continue 
            for nei in (node.left, node.right, node.parent): 
                if nei and nei not in vis: 
                    vis.add(nei)
                    q.append((nei,dis+1))
        return ans
