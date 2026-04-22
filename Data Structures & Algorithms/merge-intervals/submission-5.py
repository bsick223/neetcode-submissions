class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # [[1, 2], [2, 3]]

        # loop through each one, 

        res = []

        intervals.sort()

        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]
            
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])

        return output