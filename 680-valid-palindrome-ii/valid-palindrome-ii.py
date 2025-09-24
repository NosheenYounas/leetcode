class Solution:
    def validPalindrome(self, s: str) -> bool:
        l , r = 0 , len(s)-1
        while l < r :
            if s[l]!=s[r]:
                SkipL , SkipR= s[l+1:r+1], s[l:r]
                return (SkipL == SkipL[::-1] or SkipR ==SkipR[::-1] )
            l,r = l+1 ,r-1
        return True