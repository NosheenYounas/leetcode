class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        col=len(mat[0])
        row=len(mat)
        temp=[]
        result=[]

        if row*col!=r*c:
            return mat
        for i in range(row):
            for j in range(col):
                temp.append(mat[i][j])
        x=0
        for i in range(r):
            lil=[]
            for j in range(c):
                lil.append(temp[x])
                x+=1  
            result.append(lil)  
        return result 