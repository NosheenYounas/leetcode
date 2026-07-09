class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        original = nums[:]
        even_i, odd_i = 0, 1
        for i in range(len(nums)):
            if original[i] % 2 == 0:
                nums[even_i] = original[i]
                even_i += 2
            else:
                nums[odd_i] = original[i]
                odd_i += 2
        return nums

        

        