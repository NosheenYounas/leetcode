class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        #l,r=0,n-1
        k=""
        for a in s:
            if not a.isalnum():
                pass
            else:
                k=k+a
                k=k.lower()
        if k[::-1]==k:
            return( True)
        return False
       
