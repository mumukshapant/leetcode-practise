class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left=0
        right= n-1 

        leftmax, rightmax = height[left], height[right]
        area=0 

        while left<right: 
            if leftmax<rightmax: 
                left+=1 
                leftmax = max(leftmax, height[left])
                area += leftmax - height[left]
            else: 
                right-=1
                rightmax = max(rightmax, height[right])
                area+= rightmax - height[right]
        return area

                
            




        # leftmax = [0]*n
        # rightmax = [0]*n 
       

        # leftmax[0] = height[0]
        # rightmax[n-1] = height[n-1]

        # for i in range(1,n): 
        #     leftmax[i] = max(leftmax[i-1],height[i])
        # for i in range(n-2, -1, -1): 
        #     rightmax[i] = max(rightmax[i+1], height[i])
        # ans=0
        # res=0
        # for i in range(n): 
        #     ans += min(leftmax[i], rightmax[i]) - height[i]
        # return ans 

        