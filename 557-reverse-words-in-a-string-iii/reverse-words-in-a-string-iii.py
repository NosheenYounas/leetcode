class Solution:
    def reverseWords(self, s: str) -> str:
        k=s.split()
        p=""
        for i in range(len(k)):
            p=p+k[i][::-1]+" "
        return p.rstrip()
            
        #