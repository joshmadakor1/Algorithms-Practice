'''
    Merge Overlapping Intervals:
    Write a function that takes in a an array of arbitrary intervals, merge
    any overlapping intervals, and return the new intervals in no particular
    order

    Time:  O(N), where N is the number of intervals in the input array
    Space: O(N), where N is the size of the returned intervals

    Last Practiced: 2022-03-18 06:45:32
'''
def mergeOverlappingIntervals(intervals):
    intervals = sorted(intervals, key = lambda x:x[0])
    mergedIntervals = []
    currentInterval = intervals[0]
    
    for i in range(1, len(intervals)):
        if currentInterval[1] >= intervals[i][0]:
            if currentInterval[1] < intervals[i][1]:
                currentInterval = [currentInterval[0], intervals[i][1]]
        else:
            mergedIntervals.append(currentInterval)
            currentInterval = intervals[i]
    
    mergedIntervals.append(currentInterval)
    return mergedIntervals