class Solution(object):
    def findItinerary(self, tickets):
        

        adj = {}

        # sort in reverse so we can pop smallest lexicographic destination from the end
        tickets.sort(reverse=True)
        #print(tickets)

        for src, dst in tickets:
            if src not in adj:
                adj[src] = []
            adj[src].append(dst)
        print(adj)
        res = []

        def dfs(src):
            while src in adj and adj[src]:
                next_dst = adj[src].pop()
                dfs(next_dst)
            res.append(src)

        dfs("JFK")
        return res[::-1]