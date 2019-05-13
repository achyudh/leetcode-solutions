class Solution {
    int[][] memo;
    String word1, word2;
    
    public int deleteDistance(int ptr1, int ptr2) {
        if (ptr1 >= word1.length())
            return word2.length() - ptr2;
        else if (ptr2 >= word2.length())
            return word1.length() - ptr1;
        
        if (memo[ptr1][ptr2] == -1) {
            
            if (word1.charAt(ptr1) == word2.charAt(ptr2))
                memo[ptr1][ptr2] = deleteDistance(ptr1 + 1, ptr2 + 1);
            
            else {
                int dist1 = deleteDistance(ptr1 + 1, ptr2);
                int dist2 = deleteDistance(ptr1, ptr2 + 1);
                memo[ptr1][ptr2] = 1 + Math.min(dist1, dist2);    
            }   
        }
        
        return memo[ptr1][ptr2];
    }
    
    public int minDistance(String word1, String word2) {
        this.word1 = word1;
        this.word2 = word2;
        
        this.memo = new int[word1.length()][word2.length()];
        for (int[] row : memo)
            Arrays.fill(row, -1);
        
        return deleteDistance(0, 0);
    }
}
