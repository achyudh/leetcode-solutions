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
    TreeNode node;
    int height;
    
    NodePair(TreeNode node, int height) {
        this.node = node;
        this.height = height;
    }
}

class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> traversal = new ArrayList<>();
        List<Integer> currentLevel = new ArrayList<>();
        LinkedList<NodePair> queue = new LinkedList<>();
        int prevHeight = 0;
        
        if (root != null)
            queue.addLast(new NodePair(root, 0));
        
        while(!queue.isEmpty()) {
            NodePair currentPair = queue.pollFirst();
            TreeNode currentNode = currentPair.node;
            int height = currentPair.height;
            
            if (height != prevHeight) {
                traversal.add(currentLevel);
                currentLevel = new ArrayList<>();
                prevHeight = height;
            }
            
            currentLevel.add(currentNode.val);
            
            if (currentNode.left != null)
                queue.add(new NodePair(currentNode.left, height + 1));
            
            if (currentNode.right != null)
                queue.add(new NodePair(currentNode.right, height + 1));
        }
        
        if (currentLevel.size() > 0)
            traversal.add(currentLevel);
        
        return traversal;
    }
}
