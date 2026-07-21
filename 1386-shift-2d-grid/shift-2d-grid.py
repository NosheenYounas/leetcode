class Solution:
    def shiftGrid(self, matrix: List[List[int]], k: int) -> List[List[int]]:
        M , N = len(matrix) , len(matrix[0]) 
        def postToval(r,c):
            return r*N+c
        def valTopos(v):
            return [v//N, v%N]
        res = [[0]*N for i in range(M)] 
        for r in range(M):
            for c in range(N):
                newVal = (postToval(r,c)+k) % (M*N)
                newR , newC = valTopos(newVal)
                res[newR][newC] = matrix[r][c]
        return res 