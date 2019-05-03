# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda x: (x.start, x.end))
        m_intervals = [Interval(intervals[0].start, intervals[0].end)]
        for c_int in intervals[1:]:
            if c_int.end > m_intervals[-1].end:
                if c_int.start <= m_intervals[-1].end:
                    m_intervals[-1].end = c_int.end
                else:
                    m_intervals.append(c_int)
        return m_intervals
