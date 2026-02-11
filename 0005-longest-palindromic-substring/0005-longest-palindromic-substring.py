class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        l,r =0 , 0 
        n = len(s)
        res=[]

        for i in range (n): 
            l=i
            r=i+1

            while l>=0 and r<n and s[l]==s[r]:

                if len(s[l:r+1]) > len(res):
                    res = s[l:r+1]
                l-=1
                r+=1
            

            l=i
            r=i
            while l>=0 and r<n and s[l]==s[r]: 
                if len(s[l:r+1])> len(res): 
                    res = s[l:r+1]
                l-=1
                r+=1
        return res


        
        