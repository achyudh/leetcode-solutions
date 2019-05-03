class Solution {
    public void islandVisitor(char[][] grid, int i0, int j0) {
        int n = grid.length;
        int m = grid[0].length;

        grid[i0][j0] = 0;
        if (i0 > 0 && grid[i0 - 1][j0] == '1')
            islandVisitor(grid, i0 - 1, j0);
        if (i0 < n - 1 && grid[i0 + 1][j0] == '1')
            islandVisitor(grid, i0 + 1, j0);
        if (j0 > 0 && grid[i0][j0 - 1] == '1')
            islandVisitor(grid, i0, j0 - 1);
        if (j0 < m - 1 && grid[i0][j0 + 1] == '1')
            islandVisitor(grid, i0, j0 + 1);     
    }
    
    public int numIslands(char[][] grid) {
        int n = grid.length;
        if (n == 0)
            return 0;
        
        int m = grid[0].length;
        int count = 0;
        
        for (int i0 = 0; i0 < n; i0++)
            for (int j0 = 0; j0 < m; j0++)
                if (grid[i0][j0] == '1') {
                    islandVisitor(grid, i0, j0);
                    count++;
                }
        
        return count;
    }
}
