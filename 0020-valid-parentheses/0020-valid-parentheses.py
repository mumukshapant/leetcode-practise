class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st=[] 
        for ch in s: 
            if ch in ['(', '{', '[']: 
                st.append(ch)
            else: 
                if not st: 
                    return False 
                top = st.pop()
                if (
                        (ch==')' and top !='(' ) or 
                        (ch==']' and top !='[' ) or 
                        (ch=='}' and top !='{' )
                    ): 
                    return False
        return len(st)==0

        