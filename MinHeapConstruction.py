'''
    Min Heap Construction:
    Build a min heap given an input array and implement the
    following functionality:

    buildHeap
    insert
    remove
    peek
    siftUp
    siftDown
    swap

    Last Practiced: 2022-03-16 07:50:50
'''
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        firstParent = (len(array) - 2) // 2
        for i in reversed(range(firstParent + 1)):
            self.siftDown(array, i, len(array) - 1)
        return array

    def siftDown(self, heap, currentIndex, endIndex):
        childOneIndex = currentIndex * 2 + 1
        while childOneIndex <= endIndex:
            childTwoIndex = currentIndex * 2 + 2 if currentIndex * 2 + 2 <= endIndex else -1
            if childTwoIndex != -1 and heap[childTwoIndex] < heap[childOneIndex]:
                indexToSwap = childTwoIndex
            else:
                indexToSwap = childOneIndex
            if heap[indexToSwap] < heap[currentIndex]:
                self.swap(heap, indexToSwap, currentIndex)
                currentIndex = indexToSwap
                childOneIndex = currentIndex * 2 + 1
            else:
                return # heap is already in built

    def siftUp(self, heap, currentIndex):
        parentIndex = (currentIndex - 1) // 2
        while parentIndex >= 0 and heap[parentIndex] > heap[currentIndex]:
            self.swap(heap, currentIndex, parentIndex)
            currentIndex = parentIndex
            parentIndex = (currentIndex - 1) // 2

    def peek(self):
        if len(self.heap) >= 1: return self.heap[0]

    def remove(self):
        self.swap(self.heap, 0, len(self.heap) - 1)
        valueToPop = self.heap.pop()
        self.siftDown(self.heap, 0, len(self.heap) - 1)
        return valueToPop

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(self.heap, len(self.heap) - 1)
        
    def swap(self, heap, left, right):
        heap[left], heap[right] = heap[right], heap[left]

myHeap = MinHeap([48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41])
print(myHeap.heap)