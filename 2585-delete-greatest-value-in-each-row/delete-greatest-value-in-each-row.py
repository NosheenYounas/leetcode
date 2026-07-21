class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(0, len(grid)):
            grid[i].sort()
        for i in range(0, len(grid[0])):
            maxi = 0
            for j in range(0, len(grid)):
                maxi = max(maxi, grid[j][i])
            ans += maxi
        return ans
        