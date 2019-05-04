class Solution {
    public String minWindow(String s, String t) {   
        HashSet<Character> satChars = new HashSet<>(); 
        HashMap<Character, Integer> target = new HashMap<>();
        HashMap<Character, Integer> currChars = new HashMap<>();
        int start = 0, end = 0, minStart = 0, minEnd = 0;
        int minSize = s.length() + 1;
        
        for (char c : t.toCharArray())
            target.put(c, target.getOrDefault(c, 0) + 1);
        
        while(end < s.length()) {
            
            while (satChars.size() < target.size() && end < s.length()) {
                if (target.containsKey(s.charAt(end))) {
                    currChars.put(s.charAt(end), currChars.getOrDefault(s.charAt(end), 0) + 1);
                    if (target.get(s.charAt(end)) <= currChars.get(s.charAt(end)))
                        satChars.add(s.charAt(end));
                    }
                end++;
            }
                        
            while (satChars.size() >= target.size() && start < end) {
                if (target.containsKey(s.charAt(start))) {
                    int count = currChars.get(s.charAt(start));
                    currChars.put(s.charAt(start), count - 1);
                    if (target.get(s.charAt(start)) > count - 1)
                        satChars.remove(s.charAt(start));
                }
                start++;
            }
            
            if (end - start + 1 < minSize) {
                minSize = end - start + 1;
                minStart = start - 1;
                minEnd = end;
            }
        }
        
        return s.substring(minStart, minEnd);
    }
}
