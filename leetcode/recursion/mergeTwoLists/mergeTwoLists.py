# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ############################################
        ### RECURSIVE SOLUTION #####################
        ############################################
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            h1 = l1
            h2 = l2
            if h1.val <= h2.val:
                h1.next = self.mergeTwoLists(l1.next, l2)
                return h1
            else:
                h2.next = self.mergeTwoLists(l1, l2.next)
                return h2


        ############################################
        ### ITERATIVE SOLUTION
        ############################################
        # head = tail = ListNode(-1)
        # while l1 and l2:
        #     if l1.val <= l2.val:
        #         tail.next = l1
        #         l1 = l1.next
        #     else:
        #         tail.next = l2
        #         l2 = l2.next
        #     tail = tail.next
        
        # if l1: tail.next = l1
        # if l2: tail.next = l2
        
        # return head.next
     
