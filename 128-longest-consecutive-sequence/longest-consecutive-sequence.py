class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        res = 1
        cur = 1

        for i in range(len(nums) - 1):
            diff = nums[i + 1] - nums[i]
            if diff == 0:
                continue  # skip duplicates, don't break the streak
            elif diff == 1:
                cur += 1
                res = max(res, cur)
            else:
                cur = 1  # streak broken, reset

        return res