/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
 
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode iter = head, prev = null, temp;
        
        while(iter != null) {
            temp = iter.next;
            iter.next = prev;
            prev = iter;
            iter = temp;
        }
        
        return prev;
    }
}
