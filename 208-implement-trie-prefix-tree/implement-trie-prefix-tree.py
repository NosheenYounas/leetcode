class TriNode:
    def __init__(self):
        self.Childern={}
        self.endofWord=False

class Trie:

    def __init__(self):
        self.root=TriNode()
    def insert(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.Childern:
                cur.Childern[c]=TriNode()
            cur=cur.Childern[c]
        cur.endofWord=True
    def search(self, word: str) -> bool:
        cur=self.root
        for c in word:
            if c not in cur.Childern:
                return False
            cur=cur.Childern[c]
        return cur.endofWord
        

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for c in prefix:
            if c not in cur.Childern:
                return False
            cur=cur.Childern[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)