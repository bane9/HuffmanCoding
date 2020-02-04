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
    def parent(index):
        return index // 2
    
    @staticmethod
    def leftChild(index):
        return 2 * index
    
    @staticmethod
    def rightChild(index):
        return (2 * index) + 1

    def isLeaf(self, index): 
        return index >= len(self) // 2

    def insert(self, value):
        self.__data.push(value)
        current = len(self) - 1
        while self[current] < self[MinHeap.parent(current)]:
            self[current], self[MinHeap.parent(current)] =  self[MinHeap.parent(current)], self[current]
            current = MinHeap.parent(current)

    def pop(self):
        return self.__data.popSecondItem()
