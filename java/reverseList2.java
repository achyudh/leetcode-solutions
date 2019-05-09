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
        
        while (iter != null) {
            temp = iter.next;
            iter.next = prev;
            prev = iter;
            iter = temp;
        }

        return prev;
    }
    
    public ListNode reverseBetween(ListNode head, int m, int n) {
        ListNode strPtr = head, strPrev = null, endPtr = head;
        
        for (int i = 1; i < m; i++) {
            strPrev = strPtr;
            strPtr = strPtr.next;
        }
        
        for (int i = 1; i < n; i++)
            endPtr = endPtr.next;            
        
        ListNode endNext = endPtr.next;
        endPtr.next = null;
        
        if (strPrev != null)
            strPrev.next = reverseList(strPtr);
        else
            head = reverseList(strPtr);
        
        strPtr.next = endNext;
        return head;
    }
}
