class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        ans=float('inf')
        for i in range(n):
            if i>0  and nums[i]==nums[i-1]:
                continue
            lo,hi = i+1,n-1
            while lo<hi:
                summ = nums[i] + nums[lo] + nums[hi]
                if abs(summ-target)<abs(ans-target):
                    ans=summ
                if summ==target:
                    return summ
                elif summ < target :
                    lo += 1
                else:
                    hi-=1
        
        return ans