class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
        adj ={ ch:set() for w in words for ch in w }
        # adj = {'w' 'r' 't' 'e' 'f'}

        for i in range(len(words)-1):
            w1,w2 = words[i] , words[i+1]
            minlen = min(len(w1), len(w2))

            if len(w1)>len(w2) and w1[:minlen] == w2[:minlen] : 
                return ""

            for j in range(minlen): 
                if w1[j] != w2[j]: 
                    adj[w1[j]].add(w2[j])
                    break 
        
        visit= {} 
        res=[]

        def dfs(ch): 
            if ch in visit: 
                return visit[ch]
            
            visit[ch]=True 

            for neighbor in adj[ch]: 
                if dfs(neighbor): 
                    return True 
            visit[ch]=False 
            res.append(ch)
        
        
        # end of function
        
        for ch in adj: 
            if dfs(ch): 
                return ""
        
        res.reverse() 
        return "".join(res)

        

                