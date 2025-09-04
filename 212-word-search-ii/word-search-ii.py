class TriNode:
    def __init__(self):
        self.childern={}
        self.isword=False
    def addword(self,word):
        cur=self
        for c in word:
            if c not in cur.childern:
                cur.childern[c]=TriNode()
            cur=cur.childern[c]
        cur.isword=True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TriNode()
        for w in words:
            root.addword(w)
        ROWS,COLS=len(board),len(board[0])
        res,visit=set(),set()
        def dfs(r,c,node,word):
            if (r<0 or c<0 or r==ROWS or c==COLS or
             board[r][c] not in node.childern or (r,c)in visit):
                return
            visit.add((r,c))
            node=node.childern[board[r][c]]
            word+=board[r][c]
            if node.isword:
                res.add(word)
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            visit.remove((r,c))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")
        return list(res)
    

        