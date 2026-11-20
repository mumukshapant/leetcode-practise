class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        int n = nums.length;                Arrays.sort(nums); 


        Set<List<Integer>> set = new HashSet<>();

        // i+j+k=0
        int sum = 0;


        for (int i = 0; i < n; i++) {
            sum = 0 - nums[i];
            int j = i + 1, k = n - 1;
            while (j < k) {
                if (nums[j] + nums[k] == sum) {
                    set.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    j++; k--;
                }
                else if (nums[j] + nums[k]< sum)
                    j++;
                else
                    k--;

            }
        }
        return new ArrayList<>(set);

    }
}