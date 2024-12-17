class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        S=Counter(s)
        T=Counter(t)
        for c in S:
            if S[c]!=T[c]:
                return False
        return True