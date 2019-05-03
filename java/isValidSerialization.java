class Solution {
    public boolean isValidSerialization(String preorder) {
        String[] input = preorder.split(",");
        Deque<String> stack = new ArrayDeque<String>();
        
        int iter = 1;
        stack.push(input[0]);
        while (!stack.isEmpty() && iter < input.length) { 
            if (input[iter].equals("#")) {
                while (!stack.isEmpty() && stack.peek().equals("#")) {
                    if (stack.size() < 2)
                        return false;
                    stack.pop();
                    stack.pop();
                }
            }
            stack.push(input[iter]);
            iter++;
        }
        String last = stack.pop();
        return stack.isEmpty() && last.equals("#");
    }
}
