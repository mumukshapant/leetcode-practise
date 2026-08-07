class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        myset = set() 
        i,j=0,0 
        maxlen=0 
        while j<len(s): 
            if s[j] in myset: 
                myset.remove(s[i])
                i+=1
            else: 

                myset.add(s[j])
                maxlen= max(j-i+1, maxlen)
                j+=1
            
        return maxlen


        