class TrieNode: 
    def __init__(self): 
        self.children={}
        self.isword=False
    
    def addword(self, word):
        curr= self
        for ch in word: 
            if ch not in curr.children: 
                curr.children[ch]=TrieNode()
            curr= curr.children[ch]
        curr.isword= True 

class Solution(object):
    def findWords(self, b, words):
        root= TrieNode()

        for w in words: 
            root.addword(w)

        m,n= len(b),len(b[0]) 
        res = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(r,c, currnode, word_visited_so_far): 
            if (r>=m or c>=n or r<0 or c<0 
            or b[r][c] not in currnode.children):  # '#' naturally fails this check
                return 

            ch = b[r][c]
            nextnode = currnode.children[ch]
            word_visited_so_far += ch

            if nextnode.isword: 
                res.add(word_visited_so_far)
                nextnode.isword = False

            b[r][c] = '#'                          # mark visited in-place
            for dr,dc in directions: 
                dfs(dr+r, dc+c, nextnode, word_visited_so_far)
            b[r][c] = ch                           # restore

            if not nextnode.children and not nextnode.isword:
                del currnode.children[ch]

        for r in range(m): 
            for c in range(n):
                dfs(r,c,root, "")

        return list(res)