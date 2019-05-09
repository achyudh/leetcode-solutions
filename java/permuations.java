class Solution {
    int[] nums;
    
    public void aggregate(List<List<Integer>> acc, List<Integer> current) {
        if (current.size() == nums.length)
            acc.add(current);
        else
            for (int i = 0; i < nums.length; i++)
                if (!current.contains(nums[i])) {
                    List<Integer> next = new ArrayList<Integer>(current);
                    next.add(nums[i]);
                    aggregate(acc, next);
                }
    }
    
    public List<List<Integer>> permute(int[] nums) {
        this.nums = nums;
        List<List<Integer>> acc = new ArrayList<List<Integer>>();
        aggregate(acc, new ArrayList<Integer>());
        return acc;
    }
}
