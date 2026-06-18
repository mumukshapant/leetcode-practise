class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0 
        n=len(s)
        charset = set()
        j=0
        maxlen=0 
        
        while j<n: 
            if s[j] not in charset : 
                charset.add(s[j])
                maxlen= max(j-i+1, maxlen)
                j+=1
            else: 
                charset.remove(s[i])
                i+=1
        return maxlen


        