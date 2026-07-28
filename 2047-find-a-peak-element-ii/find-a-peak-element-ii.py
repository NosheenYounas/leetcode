class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        index = []
        maax = 0 
        m , n = len(mat) , len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] > maax:
                    maax = mat[i][j]
                    index=[i,j]
               
                    
        return index