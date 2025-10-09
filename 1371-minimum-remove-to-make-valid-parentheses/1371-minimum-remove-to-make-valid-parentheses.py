class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        cnt = 0
        res = []
        for c in s:
            if c == "(":
                cnt +=1
                res.append(c)
            elif c == ")" and cnt>0:
                cnt -= 1
                res.append(c)
            elif c != ")":
                res.append(c)
        filtered =[]
        for c in res[::-1]:
            if cnt>0 and c== "(":
                cnt -=1
            else:
                filtered.append(c)
        return "".join(filtered[::-1])


                

                