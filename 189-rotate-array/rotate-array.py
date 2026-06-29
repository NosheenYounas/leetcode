class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n                          # handle k >= n
        nums.reverse()                  # whole array
        nums[:k] = reversed(nums[:k])   # first k
        nums[k:] = reversed(nums[k:]) 
