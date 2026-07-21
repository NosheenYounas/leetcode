class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()
        n = len(grid[0])
        ans = 0 
        for j in range(n):
            ans += max(row[j] for row in grid)
        return ans
        
        