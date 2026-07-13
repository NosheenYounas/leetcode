class Solution:
    def getFactors(self, n: int,start: int = 2) -> List[List[int]]:
        res = []
        for i in range(start, int(n**0.5) + 1):
            if n % i == 0:
                res.append([i, n//i])
                for sub in self.getFactors(n//i, i):
                    res.append([i] + sub)
            else:
                continue
        return res