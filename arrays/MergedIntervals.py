"""2. Merged Intervals

Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return 
an array of the non-overlapping intervals 
that cover all the intervals in the input.

"""


def mergedIntervals(intervals):
    merged = []
    tempInterval = intervals[0]
    for i in range(1, len(intervals)):
        if(tempInterval[1] >= intervals[i][0]):
            tempInterval[1] = max(tempInterval[1], intervals[i][1])
        else:
            merged.append(tempInterval)
            tempInterval = intervals[i]
    merged.append(tempInterval)
    return merged


print(mergedIntervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
