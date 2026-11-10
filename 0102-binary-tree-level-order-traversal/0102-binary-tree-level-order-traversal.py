# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root: 
            return []
        q=deque([root])
        res=[]
        while q: 
            qlen= len(q)
            level=[] 
            for i in range(qlen): 
                currnode= q.popleft() 
                level.append(currnode.val)
                if currnode.left: 
                    q.append(currnode.left)
                if currnode.right: 
                    q.append(currnode.right)
            res.append(level)
        return res