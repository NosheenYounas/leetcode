class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n*2
        for i, a in enumerate(nums):
            ans[i]= ans[i+n] = a
        return ans

        