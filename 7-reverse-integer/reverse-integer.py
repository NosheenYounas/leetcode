class Solution:
    def reverse(self, x: int) -> int:
        
        if x <0:
            x=abs(x)
            s=str(x)
            k=int(s[::-1])
            if k>2**31:
                return 0
            return -k
        else:
             s=str(x)
             k=int(s[::-1])
             if k>2**31:
                return 0
        return k
