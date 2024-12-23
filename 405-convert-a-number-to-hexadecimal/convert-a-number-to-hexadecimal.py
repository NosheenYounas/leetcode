class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return "0"
        hexi = '0123456789abcdef'
        ans=""
        for i in range(8):
            ans=hexi[num%16]+ans
            num=num//16
        return ans.lstrip('0')

        