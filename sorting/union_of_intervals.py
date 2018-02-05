from collections import namedtuple

Endpoint = namedtuple("Endpoint", ('time', 'is_closed'))
class Interval :
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __lt__(self, other):
        if self.left.time != other.left.time :
            return self.left.time < other.left.time
        return self.left.is_closed and not other.left.is_closed

def union_of_intervals(intervals):
    intervals.sort()
    merged_intervals = []
    for interval in intervals :
        if not merged_intervals :
            merged_intervals.append(interval)
        elif interval.left.time < merged_intervals[-1].right.time or interval.left.time == merged_intervals[-1].right.time and (merged_intervals[-1].right.is_closed or interval.left.closed):
            if merged_intervals[-1].right.time < interval.right.time or  merged_intervals[-1].right.time == interval.right.time and interval.right.is_closed :
                merged_intervals[-1].right = interval.right 
        else:
            merged_intervals.append(interval)
    return merged_intervals
