# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        '''
        STEP 1: Create a min heap
         - Put the first node of every non-empty list into the heap

        STEP 2: Create a dummy node
            - This helps us build the final merged linked list easily

        STEP 3: While heap is not empty

            (3.1) Pop the smallest node from the heap

            (3.2) Attach this node to the result list

            (3.3) If this popped node has a next node
                - push that next node into the heap

        STEP 4: Return dummy.next
            - this is the head of the merged list
        '''
        
        minheap =[] 
        dummy = ListNode(-1)
        curr = dummy 

        for index, node in enumerate(lists):
            if node : 
                heapq.heappush(minheap, (node.val, index, node) )
        
        while minheap: 
            value, index, node = heapq.heappop(minheap)
            curr.next = node 
            curr=curr.next 

            if node.next: 
                heapq.heappush(minheap, (node.next.val, index, node.next))
            
        return dummy.next








