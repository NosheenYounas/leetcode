class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for A in image:
            A.reverse()
            for i in range(len(A)):
                A[i] ^= 1
        return image
        
        