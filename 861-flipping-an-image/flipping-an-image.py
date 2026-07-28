class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        m , n = len(image), len(image[0])
        output = [[0]*m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if image[i][j] == 1:
                    output[i][j] =0
                else:
                    output[i][j] =1
        for row in range(m):
            output[row].reverse()
        return output
        