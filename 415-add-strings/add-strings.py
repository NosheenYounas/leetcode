class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        res = []
        carry = 0
        while i >= 0 or j >= 0:
            cur_i=int(num1[i]) if i>=0 else 0
            cur_j=int(num2[j]) if j>=0 else 0
            cur_sum=carry+cur_i+cur_j
            res.append(str(cur_sum % 10))
            carry =cur_sum//10
            i -= 1
            j -= 1
        if carry:
            res.append(str(carry))
        return ''.join(reversed(res))