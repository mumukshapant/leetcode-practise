class Solution(object):
    def carFleet(self, t, pos, sp):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """

        pair = [(p,s) for p,s in zip(pos, sp)]
        pair.sort(reverse=True)

        prevtime = (t-pair[0][0])/pair[0][1]
        fleet=1 

        for i in range(1,len(pair)): 
            currtime = (t-pair[i][0])/pair[i][1]
            if currtime>prevtime : 
                fleet+=1
                prevtime= currtime 
        return fleet
        
