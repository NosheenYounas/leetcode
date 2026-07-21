class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m , n = len(grid) , len(grid[0])
        row_ones , col_ones = [0]*m , [0]*n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_ones[i] +=1
                    col_ones[j] +=1
        diff = [[0]*n for _ in range(m)]
        for i in range(m):
            for j  in range(n):
                row_ones_i = row_ones[i]
                col_ones_j = col_ones[j]
                row_zeros_i = m-row_ones_i 
                col_zeros_j = n-col_ones_j
                diff[i][j] = row_ones_i+col_ones_j- row_zeros_i -col_zeros_j
        return diff



                    