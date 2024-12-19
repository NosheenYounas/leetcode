class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if nums is None:
            return
        
        n = list(set(nums))
        if len(n)<3:
            return max(n)
        else:
            return sorted(n)[-3]
        