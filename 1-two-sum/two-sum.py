class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        for a,b in  enumerate(nums):
            diff = target - b
            if diff in mapp:
                return [mapp[diff],a]

            else:
                mapp[b]= a
        