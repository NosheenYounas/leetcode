class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        output=[]
        m , n = len(matrix) , len(matrix[0])
        for i in range(m):
            for j in range(n):
                output.append(matrix[i][j])
        output.sort()
        return output[k-1]