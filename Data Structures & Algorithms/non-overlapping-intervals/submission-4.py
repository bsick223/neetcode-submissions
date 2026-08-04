class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0
        lastStart = intervals[0][0]
        lastEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if start < lastEnd:
                if end < lastEnd:
                    lastEnd = end
                res += 1
            else:
                lastEnd = end
            
        return res