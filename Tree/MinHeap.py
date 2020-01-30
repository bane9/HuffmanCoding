from Tree.List import List

class MinHeap:
    def __init__(self):
        self.__data = List()
        self.__data.push(float("-inf"))

    def __len__(self):
        return len(self.__data)
    
    def __getitem__(self, i):
        return self.__data[i]
    
    def __setitem__(self, i, value):
        self.__data[i] = value

    def clear(self):
        self.__data.clear()
        self.__data.push(float("-inf"))
    
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
        current = self.available()
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

    def pop(self):
        temp = self.__data.popSecondItem()
        self.minHeapify(len(self) - 1)
        return temp

    def available(self):
        return len(self) - 1
