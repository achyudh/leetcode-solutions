class Solution {
    public List<Integer> grayCode(int n) {
        double limit = Math.pow(2, n);
        ArrayList<Integer> result = new ArrayList<Integer>();
        for (int i = 0; i < limit; i++) {
            result.add(i ^ (i >> 1));
        }
        return result;
    }
}
