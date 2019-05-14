/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class NodePair {
    public TreeNode node;
    public int height;
    
    public NodePair(TreeNode node, int height) {
        this.node = node;
        this.height = height;
    }
}

class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> traversal = new ArrayList<>();
        LinkedList<Integer> currentLevel = new LinkedList<>();
        LinkedList<NodePair> queue = new LinkedList<>();
        int prevHeight = 0;
        
        if (root != null)
            queue.add(new NodePair(root, 0));
        
        while (!queue.isEmpty()) {
            NodePair currentPair = queue.poll();
            TreeNode currentNode = currentPair.node;
            
            if (currentPair.height != prevHeight) {
                traversal.add(currentLevel);
                currentLevel = new LinkedList<>();
                prevHeight++;
            }
            
            if (currentPair.height % 2 == 0)
                currentLevel.addLast(currentNode.val);
            else 
                currentLevel.addFirst(currentNode.val);
            
            if (currentNode.left != null)
                queue.add(new NodePair(currentNode.left, currentPair.height + 1));
            
            if (currentNode.right != null)
                queue.add(new NodePair(currentNode.right, currentPair.height + 1));
        }
        
        if (currentLevel.size() > 0)
            traversal.add(currentLevel);
        
        return traversal;
    }
}
