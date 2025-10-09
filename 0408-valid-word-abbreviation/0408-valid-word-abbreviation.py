class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j =0
        n , m = len(word) , len(abbr)
        while i < n and j < m:
            if abbr[j] == '0':
                return False
            elif word[i] == abbr[j]:
                i , j = i+1 ,j+1
            elif abbr[j].isalpha() or abbr[j] == "0":
                return False
            else:
                Sublen = 0
                while j< m and abbr[j].isdigit():
                    Sublen = Sublen*10 +int(abbr[j])
                    j += 1
                i += Sublen
        return i ==n and j ==m
            
                    







    #Time complexity: O(n+m)
    #Space complexity: O(1)