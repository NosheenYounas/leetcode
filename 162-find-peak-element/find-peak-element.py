class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
       
        maxx=max(nums)
        for i in range(len(nums)):
            if (nums[i])==maxx:
                return i
        