/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public boolean isValidNode(TreeNode node, long min, long max) {
        return (node == null) || (node.val > min && node.val < max 
                                  && isValidNode(node.left, min, node.val) 
                                  && isValidNode(node.right, node.val, max));
    }
    
    public boolean isValidBST(TreeNode root) {
        return isValidNode(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
}
