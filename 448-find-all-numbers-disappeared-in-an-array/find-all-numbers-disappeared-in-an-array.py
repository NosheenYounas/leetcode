class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
         ret = set(range(1, len(nums)+1))
         ret = ret - set(nums)
         return list(ret)