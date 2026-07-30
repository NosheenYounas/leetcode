class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        k = len(s) // 2
        vowel = "aeiouAEIOU"
        return sum(c in vowel for c in s[:k]) == sum(c in vowel for c in s[k:])
        