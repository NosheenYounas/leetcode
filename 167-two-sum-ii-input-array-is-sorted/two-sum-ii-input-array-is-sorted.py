class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums=numbers
        indexmap={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in indexmap:
                return [indexmap[diff]+1,i+1]
            indexmap[n]=i
        return 