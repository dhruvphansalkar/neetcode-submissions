class Solution {
    private HashMap<ArrayList<Integer>, Integer> map = new HashMap<>();

    public int orangesRotting(int[][] grid) {
        int count = 0;
        final int[] minutesWrapper = {0};
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 2) {
                    calculateMinutes(i - 1, j, grid, 1);
                    calculateMinutes(i + 1, j, grid, 1);
                    calculateMinutes(i, j - 1, grid, 1);
                    calculateMinutes(i, j + 1, grid, 1);
                } else if (grid[i][j] == 1) {
                    count++;
                }
            }
        }

        map.forEach((key, value) -> {
            if (value > minutesWrapper[0]) {
                minutesWrapper[0] = value;
            }
        });

        if (count > map.size()) {
            return -1;
        } else if (count == 0) {
            return 0;
        }

        return minutesWrapper[0];
    }

    public void calculateMinutes(int i, int j, int[][] grid, int minutes) {
        if (i < 0 || j < 0 || i == grid.length || j == grid[0].length 
            || grid[i][j] == 2 || grid[i][j] == 0) {
            return;
        }

        ArrayList<Integer> list = new ArrayList<>(Arrays.asList(i, j));
        if (!map.containsKey(list) || map.get(list) > minutes) {
            map.put(list, minutes);
        } else {
            return;
        }

        calculateMinutes(i - 1, j, grid, minutes + 1);
        calculateMinutes(i + 1, j, grid, minutes + 1);
        calculateMinutes(i, j - 1, grid, minutes + 1);
        calculateMinutes(i, j + 1, grid, minutes + 1);

    }
}