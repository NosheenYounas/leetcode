class Solution:
    def isHappy(self, n: int) -> bool:
        v=set()
        while n not in v:
            v.add(n)
            n=self.sumofsquares(n)
            if n==1:
                return True
        return False
    def   sumofsquares(self, n: int)  -> int:  
        out=0
        while n!=0:
            d=n%10
            d=d**2
            out+=d
            n=n//10
        return out

