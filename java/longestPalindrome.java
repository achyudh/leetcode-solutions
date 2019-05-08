class Solution {
    public String longestPalindrome(String s) {
        int[][] isPdrome = new int[s.length()][s.length()];
        int maxLen = 1, maxStart = 0;
        
        if (s.length() == 0)
            return "";
        
        for (int start = 0; start < s.length(); start++)
            isPdrome[start][start] = 1;
                
        for (int start = 0; start < s.length() - 1; start++)
            if (s.charAt(start) == s.charAt(start + 1)) {
                isPdrome[start][start + 1] = 1;
                maxStart = start; maxLen = 2;
            }
        
        for (int len = 3; len <= s.length(); len++) {
            for (int start = 0; start <= s.length() - len; start++) {
                if (isPdrome[start + 1][start + len - 2] == 1 && s.charAt(start) == s.charAt(start + len - 1)) {
                    isPdrome[start][start + len - 1] = 1;   
                    if (len > maxLen) {
                        maxStart = start; maxLen = len;       
                    }                       
                }
            }
        }
        
        return s.substring(maxStart, maxStart + maxLen);
    }
}
