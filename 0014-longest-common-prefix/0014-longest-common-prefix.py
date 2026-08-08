class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: 
            return ""
        
        minlen = min(len(x) for x in strs) #4 
        l,h = 1, minlen

        while l<=h: 
            mid = h+(l-h)//2
            
            if self.iscommonprefix(strs, mid): 
                l=mid+1
            else: 
                h = mid-1
        return strs[0][:(l+h)//2]
    
    def iscommonprefix(self, strs, l):
        str1 = strs[0][:l]

        for i in range(1,len(strs)): 
            if not strs[i].startswith(str1):
                return False
        return True 


