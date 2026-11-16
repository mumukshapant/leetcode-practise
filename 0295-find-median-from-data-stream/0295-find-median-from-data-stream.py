class MedianFinder(object):
    # this approach works even when numbers are unsorted
    # If we have a million numbers, we cannot sort them because sorting is expensive, so instead, we're dividing it in half. 
    # median becomes -- largest in left and smallest in right(for even )
    # If odd number of elements, then only left can have exctra element (and that will eventually be our median ) 

    def __init__(self):
        self.minheap=[]
        self.maxheap=[] 


    def addNum(self, num):
        heapq.heappush(self.maxheap, -num)
        largestinleft=-heapq.heappop(self.maxheap)
        heapq.heappush(self.minheap, largestinleft)

        if len(self.minheap)>len(self.maxheap): 
            smallestinright =heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap,-smallestinright)
        

    def findMedian(self):
        #even 
        if len(self.maxheap)==len(self.minheap): 
            med = (self.minheap[0]+(-self.maxheap[0]) )/2.0
            return med 
        
        #odd
        return float(-self.maxheap[0])