# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(-1)
        curr = dummy
        carry = 0 

        while l1 or l2: 
            v1 = l1.val if l1 else 0 
            v2 = l2.val if l2 else 0 

            currsum = v1+v2 + carry 
            carry = currsum/10                   # 12/10 = 1
            curr.next = ListNode(currsum%10)              # 12%10 = 2
            if l1: 
                l1 = l1.next 
            if l2 : 
                l2= l2.next 
            
            curr= curr.next
            
            if carry >0 : 
                curr.next = ListNode(carry) 

        return dummy.next
            