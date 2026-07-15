class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key= lambda x:x[0])
        for i in range(1,len(intervals)):
            prevend = intervals[i-1][1]
            curr = intervals[i][0]
            if curr < prevend:
                return False
            
        return True
        
        