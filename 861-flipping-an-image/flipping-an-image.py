class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        result = []
        for row in A:
            result.append(list(map(lambda x: 0 if x == 1 else 1, row[::-1])))
        return result