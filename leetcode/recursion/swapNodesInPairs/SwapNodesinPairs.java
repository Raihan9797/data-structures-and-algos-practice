// https://leetcode.com/explore/learn/card/recursion-i/250/principle-of-recursion/1681/

/**
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
    public ListNode swapPairs(ListNode head) {
        /*
        base case: head = [] or [1]
        returns [] or [1]
        ie return the head itself
        */
        if ( head == null || head.next == null) {
            return head;
        } else {
            // recursive case
            ListNode new_tail = new ListNode(head.val, swapPairs(head.next.next));
            ListNode new_head = new ListNode(head.next.val, new_tail);
            return new_head;
        }

    }
}

/*
1. create a new_head node which uses the head.next.val and joins the the old head

2. the recursive step: we assume the upcoming nodes have been swapped using the recursive functions too! ie
swapPairs(head.next.next)

3. So we connect that with the old head!

*/