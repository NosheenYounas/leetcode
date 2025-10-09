class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        index = 0
        for i in range(len(nums)-1):
            if nums[i+1]> nums[i]:
                index = i+1
        return index
