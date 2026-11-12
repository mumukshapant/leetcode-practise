class StockPrice(object):

    def __init__(self):
        self.mapping={}
        self.maxheap, self.minheap=[],[]
        self.maxtime=0


    def update(self, timestamp, price):
    
        self.mapping[timestamp]=price
        self.maxtime= max(self.maxtime, timestamp)

        heapq.heappush(self.minheap,(price, timestamp))
        heapq.heappush(self.maxheap,(-price, timestamp))


    def current(self):
    
        return self.mapping[self.maxtime]

        

    def maximum(self):
        price, timestamp = self.maxheap[0]
        while -price != self.mapping[timestamp]:
            heappop(self.maxheap)
            price, timestamp = self.maxheap[0]
        return -price

    def minimum(self):
      
        price, timestamp = self.minheap[0]

        # Pop pairs from heap with the price doesn't match with hashmap.
        while price != self.mapping[timestamp]:
            heappop(self.minheap)
            price, timestamp = self.minheap[0]
    
        return price
