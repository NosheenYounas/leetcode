class Solution:
    def isValid(self, s: str) -> bool:
        Hashmap ={")":"(","}":"{","]":"["}
        stack =[]
        for c in s:
            if c in Hashmap:
                if stack and stack[-1] == Hashmap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
         




    #T O(n)
    #S O(n)
        