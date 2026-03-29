import heapq

class Solution(object):
    def mergeKLists(self, lists):

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

        # Min heap will store: (node value, unique index, node)
        # We add unique index because Python cannot compare ListNode directly
        min_heap = []

        # Push the first node of each non-empty list into heap
        for index, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, index, node))

        # Dummy node helps us build answer easily
        dummy = ListNode(0)
        tail = dummy

        # Keep taking the smallest available node
        while min_heap:
            value, index, node = heapq.heappop(min_heap)

            # Attach current smallest node to merged list
            tail.next = node
            tail = tail.next

            # If next node exists in same list, push it into heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, index, node.next))

        # Head of merged list
        return dummy.next