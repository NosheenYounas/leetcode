class Solution:
    def findComplement(self, num: int) -> int:
        x=bin(num)
        d=""
        for a in x[2:]:
            if a=="1":
                d+="0"
            else:
                d+="1"
        y=int(d,2)
        return y
    