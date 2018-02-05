from collections import namedtuple

Interval = namedtuple("Interval", ("left", "right"))

def interval_covering_problem(intervals):
    minimum_set = []
    n = len(intervals)
    if not n :
        return minimum_set
    intervals.sort(key=lambda x: x.left)
    minimum_set.append(intervals[0].right)
    for i in range(1,n):
        if intervals[i].left > minimum_set[-1] :
            minimum_set.append(intervals[i].right)
    return minimum_set

if __name__ == "__main__":
    intervals = [Interval(0,3), Interval(2,6), Interval(3,4), Interval(6,9)]
    print interval_covering_problem(intervals)