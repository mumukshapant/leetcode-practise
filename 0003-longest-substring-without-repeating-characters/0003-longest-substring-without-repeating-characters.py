class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # MP 
        lastseen={}
        st, maxlen=0,0
        for end, ch in enumerate(s): 
            if ch in lastseen and lastseen[ch]>=st: 
                st= lastseen[ch]+1
            
            lastseen[ch]=end
            maxlen= max(maxlen, end-st+1)
        return maxlen