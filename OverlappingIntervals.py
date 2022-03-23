'''
    Merge Overlapping Intervals:
    Given an array of intervals, merge them and return them in sorted/overlapped order

    Time: O(NlogN)
    Space: O(N)

    Last Practiced: 2022-03-23 06:52:48
'''
def mergeOverlappingIntervals(intervals):
    intervals = sorted(intervals, key = lambda x:x[0])
    answer = []
    currentInterval = intervals[0]
    
    for i in range(1, len(intervals)):
        if currentInterval[1] >= intervals[i][0]:
            if currentInterval[1] < intervals[i][1]:
                currentInterval = [currentInterval[0], intervals[i][1]]
        else:
            answer.append(currentInterval)
            currentInterval = intervals[i]
                
    answer.append(currentInterval)
    return answer