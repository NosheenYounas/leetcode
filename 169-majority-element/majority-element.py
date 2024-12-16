class Solution(object):
    def majorityElement(self, nums):
     nums.sort()
     mid = len(nums) // 2
        
     return nums[mid]