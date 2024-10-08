class Solution {
    public int minPathSum(int[][] grid) {

        int m = grid.length;
        int n = grid[0].length;
        int[][] dp = new int[m][n];

        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {

                // boundary condition i
                // if "i" ( row ) is last , it cannot go up only right
                if (i == m - 1 && j != n - 1)
                    dp[i][j] = grid[i][j] + dp[i][j + 1];

                // boundary condition j
                else if (j == n - 1 && i != m - 1)
                    dp[i][j] = grid[i][j] + dp[i + 1][j];

                else if (j != n - 1 && i != m - 1) {
                    int right = dp[i][j + 1];
                    int down = dp[i + 1][j];
                    dp[i][j] = grid[i][j] + Math.min(down, right);
                }

                else 
                    dp[i][j]= grid[i][j]; 

            }
        }

        return dp[0][0]; 

    }
}