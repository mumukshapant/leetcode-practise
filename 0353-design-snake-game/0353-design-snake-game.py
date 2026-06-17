class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.width= width
        self.height= height 
        self.food = food
        self.snake = deque([(0,0)])
        self.score = 0

        

    def move(self, direction):
        """
        :type direction: str
        :rtype: int
        """
        # tail ----> Head

        head_r, head_c =self.snake[-1]
        if direction=='U':
            head_r-=1
        elif direction=='D':
            head_r+=1
        elif direction=='L':
            head_c-=1
        elif direction=='R':
            head_c+=1
        else :
            return -1

        # Wall collision 
        if head_r<0 or head_c<0 or head_r>=self.height or head_c>=self.width:
            return -1

        # Food Found 
        if self.food and [head_r, head_c]==self.food[0]: 
            self.score+=1
            self.food.pop(0) #remove from beginning
        else: 
            self.snake.popleft()


        #Self collision 
        if (head_r, head_c) in self.snake: 
            return -1 
        
        # Add new head 
        self.snake.append((head_r, head_c))

        return self.score




        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)