# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row, col):
#        """
#        :type row : int, col : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        m,n = binaryMatrix.dimensions()

        def binarysearch(row): 

            lo,hi=0,n-1
            leftmost= 42789437

            while(lo<=hi): 
                mid = lo+(hi-lo)//2

                if binaryMatrix.get(row,mid)==0: 
                    lo = mid+1
                else: 
                    leftmost = mid
                    hi = mid-1
            return leftmost
        
        res=n 
        for row in range(m): 
            ind = binarysearch(row)
            res = min(res, ind)
        
        return res if res<n else -1 

        