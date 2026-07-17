class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        intervals.sort()
        res = []
        l = toBeRemoved[0]
        r = toBeRemoved[1]
        for start, end in intervals:
            if start > r  or end < l:
                res.append([start,end])
            else:
                if start < l:
                    res.append([start, l])
                if end > r:
                    res. append([r,end])
        return res