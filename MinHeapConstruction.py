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

	Last Practiced: 2022-03-10 07:22:45
'''
class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)
    
    def buildHeap(self, array):
        firstParent = (len(array) - 2) // 2
        for i in reversed(range(firstParent + 1)):
            self.siftDown(array, i, len(array) - 1)
        return array

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(self.heap, 0, len(self.heap) - 1)
        valueToRemove = self.heap.pop()
        self.siftDown(self.heap, 0, len(self.heap) - 1)
        return valueToRemove
    
    def insert(self, value):
        self.heap.append(value)
        self.siftUp(self.heap, len(self.heap) - 1)

    def siftUp(self, heap, currentIndex):
        parentIndex = (currentIndex - 1) // 2
        while currentIndex > 0 and heap[currentIndex] < heap[parentIndex]:
            self.swap(heap, currentIndex, parentIndex)
            currentIndex = parentIndex
            parentIndex = (currentIndex - 1) // 2

    def siftDown(self, heap, currentIndex, endIndex):
        childOneIndex = (currentIndex * 2 + 1)
        while childOneIndex <= endIndex:
            childTwoIndex = (currentIndex * 2 + 2) if (currentIndex * 2 + 2) <= endIndex else -1
            if childTwoIndex != -1 and heap[childTwoIndex] < heap[childOneIndex]:
                indexToSwap = childTwoIndex
            else:
                indexToSwap = childOneIndex
            if heap[indexToSwap] < heap[currentIndex]:
                self.swap(heap, currentIndex, indexToSwap)
                currentIndex = indexToSwap
                childOneIndex = (currentIndex * 2 + 1)
            else:
                return

    def swap(self, heap, left, right):
        heap[left], heap[right] = heap[right], heap[left]