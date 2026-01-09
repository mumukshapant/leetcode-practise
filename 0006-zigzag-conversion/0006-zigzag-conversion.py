class Solution(object):
    def convert(self, s, n):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if n==1 : 
            return s

        res=[]
        for row in range(n): 
            deltadown = 2*(n-1-row)
            deltaup = 2*row 
            index= row

            while index < len(s): 
                res.append(s[index])

                # first row only 
                if row==0 : 
                    index+= deltadown
                
                # last row
                elif row==n-1: 
                    index+=deltaup
                
                else: 
                    index+=deltadown
                    if index<len(s): 
                        res.append(s[index])
                    index+=deltaup
        return "".join(res)


        