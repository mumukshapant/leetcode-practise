class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # EXPAND AROUND CENTRE 
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