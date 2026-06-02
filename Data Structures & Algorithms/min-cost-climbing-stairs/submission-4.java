class Solution {
    HashMap<Integer, Integer> map = new HashMap<>();

    public int minCostClimbingStairs(int[] cost) {
        return Math.min(climbStairs(0, cost), climbStairs(1, cost));
    }

    public int climbStairs(int i, int[] cost) {
        if (map.containsKey(i)) {
            return map.get(i);
        }

        if (i >= cost.length) {
            map.put(i, 0);
            return 0;
        }

        if (i == cost.length - 1) {
            map.put(i, cost[i]);
            return cost[i];
        }

        int minCost = cost[i] + Math.min(climbStairs(i + 1, cost), climbStairs(i + 2, cost));
        map.put(i, minCost);
        return map.get(i);
    }
}
