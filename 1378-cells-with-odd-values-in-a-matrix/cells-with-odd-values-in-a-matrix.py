class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        ans = [[0] * n for _ in range(m)]
        k = len(indices)
        
        for i in range(k):
            # increment the whole row indices[i][0]
            for j in range(n):
                ans[indices[i][0]][j] += 1
            # increment the whole column indices[i][1]
            for j in range(m):
                ans[j][indices[i][1]] += 1
        
        count = 0
        for i in range(m):
            for j in range(n):
                if ans[i][j] % 2 != 0:
                    count += 1
        
        return count