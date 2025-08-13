class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_cov=[]
        while n > 0:
            remainder = n % 2
            bin_cov.append(str(remainder))
            n //= 2
        x="".join(bin_cov[::-1])
        count=0
        for i in x:
            if i=='1':
                count=count+1
        return count

