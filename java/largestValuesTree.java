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
    public List<Integer> largestValues(TreeNode root) {
        List<Integer> maxValues = new ArrayList<>();
        LinkedList<NodePair> queue = new LinkedList<>();
        
        if (root != null)
            queue.add(new NodePair(root, 0));
        else
            return maxValues;
        
        int prevHeight = 0, currentMax = root.val;
        
        while (!queue.isEmpty()) {
            NodePair currentPair = queue.poll();
            TreeNode currentNode = currentPair.node;

            if (currentPair.height != prevHeight) {
                prevHeight = currentPair.height;
                maxValues.add(currentMax);
                currentMax = currentNode.val;
            }
            
            else 
                currentMax = Math.max(currentNode.val, currentMax);
            
            if (currentNode.right != null)
                queue.add(new NodePair(currentNode.right, currentPair.height + 1));
            
            if (currentNode.left != null)
                queue.add(new NodePair(currentNode.left, currentPair.height + 1));
        }
        
        maxValues.add(currentMax);
        return maxValues;
    }
}
