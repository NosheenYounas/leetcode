class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m , n = len(mat) , len(mat[0])
        mp = {}
        for i in range(m):
            for j in range(n):
                key = i-j 
                if key not in mp:
                    mp[key]=[]
                mp[key].append(mat[i][j])
        for key in mp:
            mp[key].sort()
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                key = i-j
                mat[i][j]= mp[key].pop()
        return mat
