class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        #Refer: https://www.youtube.com/watch?v=1yEyz6IqDac
    
        def helper(node): 
            if not node: 
                return 0 
            
            leftmax = max(0, helper(node.left), 0 ) # 0 because we dont want -ve
            rightmax = max(0, helper(node.right), 0 )

            maxIfNodeIsRoot = node.val+leftmax+rightmax
            self.maxsum = max(self.maxsum, maxIfNodeIsRoot)

            return node.val+max(leftmax,rightmax)
        
        self.maxsum = float('-inf')
        helper(root)
        return self.maxsum