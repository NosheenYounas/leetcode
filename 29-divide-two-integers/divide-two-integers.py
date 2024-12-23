class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor<0 and dividend<0:
            d=abs(dividend)
            k=abs(divisor)
            j=int(d//k)
            if j>=2**31:
                j=j-1
            return j
        elif divisor<0 or dividend<0:
             d=abs(dividend)
             k=abs(divisor)
             j=int(d//k)
             return -1*j
        else:
            d=dividend
            k=divisor
            j=int(d//k)
            if j>=2**31:
                j=j-1
            return j