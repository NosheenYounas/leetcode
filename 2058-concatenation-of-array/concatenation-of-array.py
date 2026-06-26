class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = 2*n*[0]
        for i, a in enumerate(nums):
             res[i] = res[i+n] = a 
        return res

        