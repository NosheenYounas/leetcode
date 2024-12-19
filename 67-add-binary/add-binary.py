class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        res = []
        carry = 0
        while i >= 0 or j >= 0:
            cur_i=int(a[i]) if i>=0 else 0
            cur_j=int(b[j]) if j>=0 else 0
            cur_sum=carry+cur_i+cur_j
            res.append(str(cur_sum % 2))
            carry =cur_sum//2
            i -= 1
            j -= 1
        if carry:
            res.append(str(carry))
        return ''.join(reversed(res))