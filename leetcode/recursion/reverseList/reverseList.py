# https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/3233/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        elif not head.next:
            return head
        else:
            
            new_head = Solution().reverseList(head.next)
            
            head.next.next = head
            head.next = None
            
            return new_head
        