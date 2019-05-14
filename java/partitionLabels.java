class Solution {
    public List<Integer> partitionLabels(String S) {
        int[][] alphaRange = new int[26][2];
        List<Integer> partitionLengths = new ArrayList<>();

        for (int[] row : alphaRange)
            row[0] = -1;
        
        for (int i = 0; i < S.length(); i++) {
            int index = S.charAt(i) - 'a';
            if (alphaRange[index][0] == -1) {
                alphaRange[index][0] = i;
                alphaRange[index][1] = i;
            }
            else 
                alphaRange[index][1] = i;
        }
        
        Arrays.sort(alphaRange, (o1, o2) -> Integer.compare(o1[0], o2[0]));
        
        int i = 0;
        while (alphaRange[i][0] == -1)
            i++;
        
        if (i == alphaRange.length)
            return partitionLengths;

        int[] currentRange = alphaRange[i++];
        while (i < alphaRange.length) {
            
            if (alphaRange[i][0] < currentRange[1])
                currentRange[1] = Math.max(alphaRange[i][1], currentRange[1]);

            else {
                partitionLengths.add(currentRange[1] - currentRange[0] + 1);
                currentRange = alphaRange[i];
            }
                
            i++;
        }
        
        partitionLengths.add(currentRange[1] - currentRange[0] + 1);        
        return partitionLengths;
    }
}
