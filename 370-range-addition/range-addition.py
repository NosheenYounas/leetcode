class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        result = [0] * length
        for start, end, val in updates:
            result[start] += val
            if end < length - 1:
                result[end + 1] -= val
        # accumulate is the direct analog of C++ partial_sum:
        # running prefix sum in place
        return list(accumulate(result))