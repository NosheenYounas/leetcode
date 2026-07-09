class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        l = 2  # write pointer: next position to fill
        for r in range(2, len(nums)):  # read pointer: scans the array
            if nums[r] != nums[l - 2]:
                nums[l] = nums[r]
                l += 1
        return l
        