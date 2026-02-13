class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """

        # rightmost digit ( least significant digit agar 0 hai to ignore )
        # agar 1 hai toh.. 
            # agar single 1 hai, toh directly subtract kardo 
            # agar continuous 1s hai, toh add karo 


        '''
            n&1 is AND operator.
            It is used to check whether this is odd or even. 

            Even numbers end in 0, Odd number end in 1 


            n/=2 is same as n >>= 1 (bit shift) -- it discards the rightmost bit 1101 becomes 110 
        '''
        
        ans=0 

        while n>0 : 
            if n&1 ==1 : # number ends in 1 
                ans+=1 
                n/=2

                if n&1 ==1 : # number ends in 1 
                    n+=1
            
            else: #agar 0 hai toh ignore kar do 
                n/=2 # 
        
        return ans 