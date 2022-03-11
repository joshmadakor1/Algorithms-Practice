'''
    Merge Overlapping Intervals:
    Write a function that takes in a an array of arbitrary intervals, merge
    any overlapping intervals, and return the new intervals in no particular
    order

    Time:  O(N), where N is the number of intervals in the input array
    Space: O(N), where N is the size of the returned intervals

    Last Practiced: 2022-03-11 10:45:39
'''
def mergeOverlappingIntervals(intervals):
    intervals = sorted(intervals, key = lambda x:x[0])
    currentInterval = intervals[0]
    answer = []
    
    
    for i in range(1, len(intervals)):
        if currentInterval[1] >= intervals[i][0]:
            if currentInterval[1] < intervals[i][1]:
                currentInterval= [currentInterval[0], intervals[i][1]]
        else:
            answer.append(currentInterval)
            currentInterval = intervals[i]
    
    answer.append(currentInterval)
    return answer