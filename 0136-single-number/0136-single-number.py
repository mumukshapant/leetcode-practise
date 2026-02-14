class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #using property : a^a = 0 && a^0=a
        # XOR is : 

        # 0 0  |  0
        # 1 0  |  1
        # 0 1  |  1
        # 1 1  |  0 

        xor=0
        # 7,7,1

        # 0111
        # 0111
        # 0001

        for n in nums: 
            xor = xor^n
        
        return xor 
