class TriNode:
    def __init__(self):
        self.childern={} # a :trinode a hashmap
        self.word=False
class WordDictionary:

    def __init__(self):
        self.root=TriNode()
    def addWord(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.childern:
                cur.childern[c]=TriNode()
            cur=cur.childern[c]
        cur.word=True
        

    def search(self, word: str) -> bool:
        def dfs(j,root):
            cur=root
            for i in range(j,len(word)):
                c=word[i]
                if c==".":
                    for child in cur.childern.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if c not in cur.childern:
                        return False
                    cur=cur.childern[c]
            return cur.word
        return dfs(0,self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)