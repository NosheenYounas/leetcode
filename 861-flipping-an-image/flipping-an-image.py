class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[a^1 for a in reversed(x)] for x in image]
        