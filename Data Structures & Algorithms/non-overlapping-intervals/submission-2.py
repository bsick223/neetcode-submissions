class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)
        prevEnd = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):

            beg = intervals[i][0]
            end = intervals[i][1]

            # if curr doesn't overlap, update prev end

            if beg >= prevEnd:
                prevEnd = end
                continue
            else:
                prevEnd = min(prevEnd, end)
                res += 1

        return res