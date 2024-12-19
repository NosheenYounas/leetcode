class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i=j=0 #i point for array g
        while i<len(g):
            while j<len(s) and g[i]>s[j]:
                j+=1
            if j<len(s):
                i+=1
                j+=1
            else:
                break


        return i