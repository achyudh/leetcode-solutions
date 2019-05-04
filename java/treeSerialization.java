/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

public class Codec {
    
    public String serializeNode(TreeNode node) {
        if (node == null)
            return "null";
        return node.val + "," + serializeNode(node.left) + "," + serializeNode(node.right);
    }
    
    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        return serializeNode(root);
    }
    
    public TreeNode deserializeNode(ArrayDeque<String> data) {
        String currentVal = data.removeFirst();
        if (currentVal.equals("null"))
            return null;
        TreeNode node = new TreeNode(Integer.parseInt(currentVal));
        node.left = deserializeNode(data);
        node.right = deserializeNode(data);
        return node;
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        ArrayDeque<String> queue = new ArrayDeque<String>(Arrays.asList(data.split(",")));
        return deserializeNode(queue);
    }
}

// Codec object usage:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));
