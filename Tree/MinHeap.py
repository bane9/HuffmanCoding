from Tree.List import List

class MinHeap:
    def __init__(self):
        self.__data = List()
        self.__data.push(float("-inf"))

    def __len__(self):
        return len(self.__data) - 1 if len(self.__data) != 0 else 0
    
    def __getitem__(self, i):
        return self.__data[i]
    
    def __setitem__(self, i, value):
        self.__data[i] = value
    
    def __str__(self):
        return str(self.__data)
    
    @staticmethod
    def parent(value):
        return value // 2
    
    @staticmethod
    def leftChild(value):
        return 2 * value
    
    @staticmethod
    def rightChild(value):
        return (2 * value) + 1

    def isLeaf(self, pos): 
        return pos >= len(self) // 2 and pos <= len(self)

    def insert(self, value):
        self.__data.push(value)
        current = len(self)
        while self[current] < self[MinHeap.parent(current)]:
            self[current], self[MinHeap.parent(current)] =  self[MinHeap.parent(current)], self[current]
            current = MinHeap.parent(current)

    def minHeapify(self, pos):
        if not self.isLeaf(pos):
            if self[pos] > self[MinHeap.leftChild(pos)] or self[pos] > self[MinHeap.rightChild(pos)]:
                if self[MinHeap.leftChild(pos)] < self[MinHeap.rightChild(pos)]:
                    self[pos], self[MinHeap.leftChild(pos)] = self[MinHeap.leftChild(pos)], self[pos]
                    self.minHeapify(MinHeap.leftChild(pos))
                else:
                    self[pos], self[MinHeap.rightChild(pos)] = self[MinHeap.rightChild(pos)], self[pos]
                    self.minHeapify(MinHeap.rightChild(pos))
    
    def Heapify(self):
        for i in range(len(self) // 2, 0, -1):
            self.minHeapify(i)

    def pop(self):
        temp = self.__data.popAt(1)
        self.minHeapify(len(self))
        return temp
