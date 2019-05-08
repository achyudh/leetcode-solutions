/*
// Definition for a Node.
class Node {
    public int val;
    public Node next;
    public Node random;

    public Node() {}

    public Node(int _val,Node _next,Node _random) {
        val = _val;
        next = _next;
        random = _random;
    }
};
*/
class Solution {
    public Node copyRandomList(Node head) {
        HashMap<Node, Node> nextMap = new HashMap<>();
        Node ptr = head;
        
        while (ptr != null) {
            Node newNode = new Node(ptr.val, null, null);
            nextMap.put(ptr, newNode);
            ptr = ptr.next;
        }
        
        ptr = head;
        while (ptr != null) {
            Node newNode = nextMap.get(ptr);
            newNode.next = nextMap.get(ptr.next);
            newNode.random = nextMap.get(ptr.random);
            ptr = ptr.next;
        }
        
        return nextMap.get(head);
    }
}
