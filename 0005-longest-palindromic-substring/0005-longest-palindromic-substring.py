class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)
        start = 0
        max_len = 0

        for i in range(n):

            # ----- Odd length -----
            l = r = i

            while l >= 0 and r < n and s[l] == s[r]:
                curr_len = r - l + 1
                if curr_len > max_len:
                    start = l
                    max_len = curr_len
                l -= 1
                r += 1

            # ----- Even length -----
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                curr_len = r - l + 1
                if curr_len > max_len:
                    start = l
                    max_len = curr_len
                l -= 1
                r += 1

        return s[start:start + max_len]








        # l,r =0 , 0 
        # n = len(s)
        # res=[]

        # for i in range (n): 
        #     l=i
        #     r=i+1

        #     while l>=0 and r<n and s[l]==s[r]:

        #         if len(s[l:r+1]) > len(res):
        #             res = s[l:r+1] # slicing is very expensive , because it is creating a new string everytime. 
        #         l-=1
        #         r+=1
            

        #     l=i
        #     r=i
        #     while l>=0 and r<n and s[l]==s[r]: 
        #         if len(s[l:r+1])> len(res): 
        #             res = s[l:r+1]
        #         l-=1
        #         r+=1
        # return res


        
        