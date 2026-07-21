class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
    
        m = len(grid)
        n = len(grid[0])
        row_ones = [0] * m
        col_ones = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_ones[i] += 1
                    col_ones[j] += 1

        diff = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ones_row_i = row_ones[i]
                ones_col_j = col_ones[j]
                zeros_row_i = n - ones_row_i
                zeros_col_j = m - ones_col_j
                diff[i][j] = ones_row_i + ones_col_j - zeros_row_i - zeros_col_j

        return diff