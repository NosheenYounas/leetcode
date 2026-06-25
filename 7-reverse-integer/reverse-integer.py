class Solution:
    def reverse(self, x: int) -> int:
        if x <0 :
            sign  = -1
        else:
            sign = 1
        rev_no = 0
        x = abs(x)
        while x!=0 :
            digit = x% 10 
            x = x//10
            rev_no = rev_no*10 +digit
        rev_no = sign * rev_no
        if rev_no < -2**31 or rev_no > 2**31:
            return 0
        else:
            return rev_no

        