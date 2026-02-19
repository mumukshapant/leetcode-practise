class Solution(object):
    def shortestPalindrome(self,s):
        rev = s[::-1]
        temp = s + "#" + rev
        n = len(temp)
        
        # How many characters from the beginning of s are already mirrored at the end.
        arr = [0] * n
        
        for i in range(1, n):
            j = arr[i-1]
            while j > 0 and temp[i] != temp[j]:
                j = arr[j-1]
            if temp[i] == temp[j]:
                j += 1
            arr[i] = j

        # Length of longest palindromic prefix in original string
        longest_prefix = arr[-1]

        # Add remaining suffix in reverse at the front
        suffix = s[longest_prefix:]
        return suffix[::-1] + s
            