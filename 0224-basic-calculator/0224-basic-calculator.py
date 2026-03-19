class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # sign = ["+","-","(",")"]
        sign = 1 # when + , 0 when -ve
        cur,res=0,0
        st=[]

        for char in s: 
            if char in ['+','-']: 
                res += sign *cur
                sign=1 if char=='+' else -1
                cur=0

            elif char=="(": 
                
                st.append(res)
                st.append(sign)
                sign=1

                res=0 # reset every time there is an ( 
            
            elif char.isdigit(): 
                cur = cur*10+int(char)
            
            elif char==")": 
                res+=sign*cur
                res*= st.pop()
                res+= st.pop() 
                cur=0 
        
        return res+sign*cur
