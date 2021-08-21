**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        // if [] return []
        if (head == null) {
            return head;
        
        // if [1] return [1]
        } else if (head.next == null) {
            return head;
        
        // else recursive case
        } else {
            // 1 -> 2 <- 3 <- new_head
            // 2 points to null also
            // wishful thinking: assume the tail has been solved
            ListNode new_head = reverseList(head.next);
            
            // 1 <=> 2 <- 3 <- new_head
            head.next.next = head;
            
            // null <- 1 <- 2 <- 3 <- new_head
            head.next = null;
            
            // new_head -> 3 -> 2 -> 1
            return new_head;
        }
        
    }
}