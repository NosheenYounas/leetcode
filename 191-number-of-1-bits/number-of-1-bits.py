class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_cov=[]
        count=0
        while n > 0:
            remainder = n % 2
            bin_cov.append(str(remainder))
            n //= 2
            count=count+remainder 
        x="".join(bin_cov[::-1])
        return count
        
        
