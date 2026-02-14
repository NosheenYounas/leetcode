class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        for i in range(1, len(intervals)):
            prev_end = intervals[i - 1][1]
            curr_start = intervals[i][0]

            # Overlap found
            if curr_start < prev_end:
                return False
        return True

        