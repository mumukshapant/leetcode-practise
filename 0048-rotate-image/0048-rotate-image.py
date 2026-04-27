class Solution(object):
    def rotate(self, mat):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m= len(mat)
        n = len(mat[0])

        for i in range(m): 
            for j in range(i+1,n): 
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j] # in place transpose
    
        for row in mat: 
            row.reverse()
        