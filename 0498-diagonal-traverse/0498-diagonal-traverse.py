class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows,cols = len(mat) , len(mat[0])
        res =[]
       
        cur_row = cur_col = 0
        going_up =True
        while len(res) != rows * cols:
            if going_up:
                while cur_row >= 0 and cur_col < cols:
                    res.append(mat[cur_row][cur_col])
                    cur_row -= 1
                    cur_col += 1
                if  cur_col == cols:
                    cur_col -=1
                    cur_row +=2 
                else:
                    cur_row +=1
                going_up = False
            else:
                
                while cur_col >=0 and cur_row < rows:
                    res.append(mat[cur_row][cur_col])
                    cur_col -=1
                    cur_row +=1
                if cur_row == rows:
                    cur_col += 2
                    cur_row -= 1
                else:
                    cur_col +=1
                going_up = True
        return res
    #T: O(N)
    #S :O(N) if counting result as space otherwise O(1)



        