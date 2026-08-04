class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if m % 2 == 1:
                m -= 1              # align to even index

            if nums[m] == nums[m + 1]:
                l = m + 2           # pairing intact, answer is to the right
            else:
                r = m               # pairing broken, answer is at m or left

        return nums[l]
            
            
        
         
        