class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for s, e in sorted(ranges):
            if s <= left <= e:
                left = e + 1
        return left > right     