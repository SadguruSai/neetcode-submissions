class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda i:i[0])
        output=[intervals[0]]
        for start,end in intervals[1:]:
            LastEnd=output[-1][-1]
            if start<=LastEnd:
                output[-1][-1]=max(LastEnd,end)
            else:
                output.append([start,end])
        return output
