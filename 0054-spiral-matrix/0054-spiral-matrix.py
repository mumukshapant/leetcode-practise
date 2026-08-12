class Solution(object):
    def spiralOrder(self, mat):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m =len(mat)
        n = len(mat[0])

        top=0
        bottom = m-1
        left= 0
        right = n-1 
        res=[]

        while top<=bottom and left<=right: 

            # top right 
            for i in range(left, right+1) : 
                res.append(mat[top][i])
            #print(res) # [1 ,  2]

            top+=1

            #right down 
            for i in range(top,bottom+1): 
                res.append(mat[i][right])
            #print(res) # [3,6]
            right-=1

            # bottom left 
            if top<=bottom: 
                for i in range(right, left-1,-1): 
                    res.append(mat[bottom][i])
                #print(res) # [9,8]
                bottom-=1

            # left top 
            if left<=right: 
                for i in range(bottom, top-1, -1): 
                    res.append(mat[i][left])
                #print(res) #[7]
                left+=1

        return res 



