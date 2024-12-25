class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()
        if not s:
            return 0
        i=0
        sign=1
        if s[i]=="+":
            i+=1
        elif s[i]=="-":
            i+=1
            sign=-1
        parse=0
        while i<len(s):
            curr=s[i]
            if not curr.isdigit():
                break
            else:
                parse=parse*10+int(curr)
            i+=1
        parse*=sign
        if parse>2**31-1:
            return 2**31-1
        elif parse<=-2**31-1:
            return -2**31
        return parse
      
