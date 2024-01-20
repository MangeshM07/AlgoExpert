# O(n log n) time | O(n) space
def mergeOverlappingIntervals(intervals):
    intervals.sort(key=lambda i:i[0])
    mergedIntervals = [intervals[0]]

    for start, end in intervals[1:]:
        lastEnd = mergedIntervals[-1][1]
        if start > lastEnd:
            mergedIntervals.append([start,end])
        else:
            mergedIntervals[-1][1]=max(end, lastEnd)
    return mergedIntervals


intervals = [   [1, 2],
                [3, 5],
                [4, 7],
                [6, 8],
                [9, 10]
            ]

print(mergeOverlappingIntervals(intervals))
