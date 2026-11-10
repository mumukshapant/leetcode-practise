# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None: 
            return "null"
        q=deque([root])
        res=[]

        while q: 
            node= q.popleft() 
            if node: 
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("null")
        return ','.join(res)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data=="null": 
            return None

        string_split = data.split(",")
        root = TreeNode(int(string_split[0]))

        q= deque([root])
        i=1 

        while q: 
            curr = q.popleft()
            if string_split[i]!="null": 
                curr.left=TreeNode(int(string_split[i]))
                q.append(curr.left)
            i+=1

            if i<len(string_split) and string_split[i]!="null": 
                curr.right = TreeNode(int(string_split[i]))
                q.append(curr.right)
            i+=1
        return root 





# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))