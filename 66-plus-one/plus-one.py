class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        k=""
        for i in range(len(digits)):
            k=k+str(digits[i])
        g=int(k)
        g=g+1
        h=str(g)
        f=[]
        for char in h:
            f.append(int(char))
        return f
