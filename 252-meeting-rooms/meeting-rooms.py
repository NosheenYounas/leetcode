class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x:x[0])
        for i in range(1, len(intervals)):
            prev_end = intervals[i-1][1]
            curr = intervals[i][0]
            if prev_end > curr:
                return False
        return True




        