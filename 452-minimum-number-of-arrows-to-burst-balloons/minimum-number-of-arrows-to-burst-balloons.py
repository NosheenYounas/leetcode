class Solution:
    def findMinArrowShots(self, intervals: List[List[int]]) -> int: 
        intervals.sort()
        prev = intervals[0]
        res = len(intervals)
        for i in range(1,len(intervals)):
            curr = intervals[i]
            if curr[0] > prev[1]:
                prev = curr
            else:
                res -= 1
                prev = [curr[0], min(curr[1], prev[1])]
        return res
       