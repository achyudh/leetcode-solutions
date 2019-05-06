class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] results = new int[2];
        int start = 0, end = numbers.length - 1;
        
        while (start < end) {
            if (numbers[start] + numbers[end] > target)
                end--;
            else if (numbers[start] + numbers[end] < target)
                start++;
            else {
                results[0] = start + 1;
                results[1] = end + 1;
                break;
            }
        }
        
        return results;
    }
}
