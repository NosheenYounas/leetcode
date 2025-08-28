class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3=nums1+nums2
        nums3.sort()
        if len(nums3)%2!=0:
            l=len(nums3)//2
            return nums3[l]
        else:
            l=len(nums3)//2
            return (nums3[l]+nums3[l-1])/2
        