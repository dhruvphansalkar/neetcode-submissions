class Solution {
    HashMap<Integer, Integer> map = new HashMap<>();
    public int rob(int[] nums) {
        return Math.max(robHouse(0, nums), robHouse(1, nums));
    }

    public int robHouse(int i, int[] nums) {
        if (map.containsKey(i)) {
            return map.get(i);
        }

        if (i >= nums.length) {
            return 0;
        }

        int cost = nums[i] + Math.max(robHouse(i + 2, nums), robHouse(i + 3, nums));
        map.put(i, cost);

        return cost;
    }
}
