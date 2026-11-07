class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l,r=0,0
        myset=set()
        maxlen=0
        for r in range(len(s)): 
            while s[r] in myset:
                myset.remove(s[l])
                l+=1
            myset.add(s[r])
            maxlen =max(r-l+1, maxlen)
        return maxlen

