class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        
        res=""

        for s in strs: 
            res += str(len(s)) + "#" + s
        return res #-->>  5#Hello5#World

        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        res= []
        i=0 
        #       5#Hello5#World
                 
        while i<len(s): 
            j=i 
            while s[j]!="#": 
                j+=1
            length = int(s[i:j]) # 5 
            res.append(s[j+1: j+1+length] ) 
            i = j + 1 + length 
        return res






        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))