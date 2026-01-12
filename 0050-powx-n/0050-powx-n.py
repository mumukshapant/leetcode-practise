class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x==0: 
            return 0
            
        if n==0 : 
            return 1
        if n<0: 
            return 1.0/self.myPow(x, -n)
        
        if n%2==0: 
            return self.myPow(x*x, n/2)
        if n%2==1: 
            return x*self.myPow(x*x, (n-1)/2 )
        
        
        
        
