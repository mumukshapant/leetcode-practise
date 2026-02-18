class Solution(object):
    def minCost(self, b1, b2):
        """
        :type basket1: List[int]
        :type basket2: List[int]
        :rtype: int
        """
        # STEP -1 Counting Frequencies
        freq= Counter(b1)
        freq.subtract(Counter(b2))

        print(freq) # {2: 2, 4: 0, 1: -2}

        # freq[cost]==0 means they are balanced
        # freq[cost] > 0 means it has an extra of that fruit 
        # freq[cost] <0 means it has a deficiet of that fruit 
        

        # STEP 2 - Find what to sort 
        to_swap=[]
        for fruit_cost, count in freq.items() : 
            if count%2!=0:  # no solution 
                return -1 
            
            for _ in range(abs(count)//2): 
                to_swap.append(fruit_cost)
        to_swap.sort() # This list holds every fruit that is in the wrong basket. 

        # STEP 3 - Cost of swapping
        global_min = min(b1+b2)
        cost=0 

        for i in range(len(to_swap)//2): 
            direct_swap_cost = to_swap[i]

            indirect_swap_cost = 2*global_min

            cost += min(direct_swap_cost, indirect_swap_cost)
        
        return cost




        '''
        For cost of swapping, we have 2 options - one is direct swapping say (10,12) . The cost of swapping is min(10,12) = 10 
        
        Then there is another option . Swap the 10 & 12 with the global minimum value existing in both b1 and b2 
        swap 10,1 . Cost = min(10,1) = 1 
        
        Then swap 12,1. Cost = min(12,1) = 1 

        '''




        
        