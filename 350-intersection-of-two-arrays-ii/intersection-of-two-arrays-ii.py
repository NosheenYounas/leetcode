class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
       
    
        res=[]
        for a in nums2:
            if a in nums1:
                res.append(a)
                nums1.remove(a)
       
        return res