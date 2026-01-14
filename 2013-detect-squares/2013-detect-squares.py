class DetectSquares(object):

    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts= []

        

    def add(self, point):
        self.ptsCount[tuple(point)]+=1
        self.pts.append(point)
        
        

    def count(self, point):
        res=0
        px,py= point 
        for x,y in self.pts: #going through all possible diagonal points
            if (abs(py-y) != abs(px-x)) or x==px or y==py: # calculating sideways vs up/down distance. Filters out everything not a diagonal 
                continue
            #this line is executed only if a diagonal is found. If a diagonal is not found, this line is not executed because the execution jumps this line after 'continue' 
            res+=self.ptsCount[(x,py)]* self.ptsCount[(px,y)]
        
        return res

        


'''
1- Treat a chosen point as a starting corner.
2- From this starting point, the code looks at every dot and checks if it is diagonally opposite from the chosen point (starting point) 

3- A point can be a diagonal if it's the same distance sideways and up/down. Not in the same row or column.

■─────□
│     │
│     │
□─────■

👉 Finding a diagonal means:

“If these two points are opposite corners of a square, then the square might exist.”

That’s it.
It does not mean a square exists yet.


'''