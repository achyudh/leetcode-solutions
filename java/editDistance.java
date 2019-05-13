class Solution {
    int maxDistance;
    int[][] memo;
    String word1, word2;
    
    public int editDistance(int ptr1, int ptr2) {
        if (ptr1 >= word1.length() && ptr2 >= word2.length())
            return 0;
        else if (ptr1 >= word1.length())
            return word2.length() - ptr2;
        else if (ptr2 >= word2.length())
            return word1.length() - ptr1;
        
        if (memo[ptr1][ptr2] == -1) {
            int repCost = editDistance(ptr1 + 1, ptr2 + 1);
            int insCost = editDistance(ptr1, ptr2 + 1);
            int delCost = editDistance(ptr1 + 1, ptr2);
            
            int nxtCost = maxDistance;
            if (word1.charAt(ptr1) == word2.charAt(ptr2))
                nxtCost = repCost - 1;
               
            memo[ptr1][ptr2] = 1 + Math.min(Math.min(repCost, insCost), Math.min(delCost, nxtCost));
        }
        
        return memo[ptr1][ptr2];
    }
    
    public int minDistance(String word1, String word2) {
        this.word1 = word1;
        this.word2 = word2;
        this.maxDistance = word1.length() + word2.length();
        this.memo = new int[word1.length()][word2.length()];
        
        for (int[] row : memo)
            Arrays.fill(row, -1);
        
        return editDistance(0, 0);
    }
}
