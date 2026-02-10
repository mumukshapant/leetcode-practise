# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        
        
        # return pair [ with_root, without_root ]
        def dfs(root): 
            if not root: 
                return [0,0]
            
            leftpair = dfs(root.left)
            rightpair = dfs(root.right)

            withroot= root.val + leftpair[1]  +rightpair[1]
            withoutroot = max(leftpair)+max(rightpair)

            return [withroot, withoutroot ]
        
        return max(dfs(root))

        # Space Complexity : O(n) 
        # Time Complexity : O(N) 





