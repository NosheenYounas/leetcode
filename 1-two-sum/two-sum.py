class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dick = {}
        for i,n in enumerate(nums):
            k = target - n 
            if k in dick:
                return [dick[k],i]
            dick[n] = i
