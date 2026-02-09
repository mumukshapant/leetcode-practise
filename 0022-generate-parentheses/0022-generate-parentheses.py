class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        curr=[]
        res=[]

        def helper(open, closed): 
            # base case 
            if open==n and closed==n : 
                res.append("".join(curr))
                return res 
            
            if open> closed : #add closed . We can add closed ) only when open is greater than closed. 
                curr.append(")")
                helper(open , closed+1 )
                curr.pop()
            if open<n : 
                curr. append("(")
                helper(open+1, closed)   
                curr.pop()

        helper(0,0)
        return res