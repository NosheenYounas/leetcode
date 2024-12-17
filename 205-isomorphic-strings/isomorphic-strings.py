class Solution(object):
    def isIsomorphic(self, s, t):
        mapSt,mapTS={},{}
        for c1,c2 in zip(s,t):
            if((c1 in mapSt and mapSt[c1]!=c2) or (c2 in mapTS and mapTS[c2]!=c1)):
                return False
            mapSt[c1]=c2
            mapTS[c2]=c1
        return True

        
        