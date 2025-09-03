class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        PosDiag=set()
        negDiag=set()
        res=[]
        board=[["."]*n for i in range(n)]
        def backtrack(r):
            if r==n:
                copy=["".join(row) for row in board]
                res.append(copy)
                return 
            for c in range(n):
                if c in col or (r+c) in PosDiag or (r-c) in negDiag:
                    continue
                col.add(c)
                PosDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c]="Q"

                backtrack(r+1)

                col.remove(c)
                PosDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c]="."
        backtrack(0)
        return res

        