class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 : 
            return False
        num=x
        rev=0

       

        while num>0 : 
            rem = num%10 #1 
            rev=rev*10+rem 
            num=num//10 # 12

        return rev==x

