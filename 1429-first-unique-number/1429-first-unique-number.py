class FirstUnique(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.q = deque()
        self.freq ={}

        for num in nums: 
            self.add(num)


    def showFirstUnique(self):
        """
        :rtype: int
        """
        while self.q and self.freq[self.q[0]]>1 :
            self.q.popleft() # remove duplicates
        if self.q: 
            return self.q[0]
        
        return -1 

    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.q.append(value)
        if value in self.freq: 
            self.freq[value]+=1
        else: 
            self.freq[value]=1 
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)