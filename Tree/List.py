from Tree.Node import Node

class List:
    def __init__(self):
        self.__head = None
        self.__size = 0
    
    def push(self, value):
        self.__size += 1
        if self.__head == None:
            self.__head = Node(value)
        else:
            temp = self.__head
            while temp.nextNode is not None:
                temp = temp.nextNode
            temp.nextNode = Node(value)
    
    def __len__(self):
        return self.__size
    
    def clear(self):
        self.__size = 0
        self.__head = None

    def __getitem__(self, i):
        if i < 0 or i > self.__size - 1:
            raise IndexError("Out of range")
        temp = self.__head
        for _ in range(i):
            temp = temp.nextNode
        return temp.data

    def __setitem__(self, i, value):
        if i < 0 or i > self.__size - 1:
            raise IndexError("Out of range")
        temp = self.__head
        for _ in range(i):
            temp = temp.nextNode
        temp.data = value

    def popSecondItem(self):
        temp = self.__head.nextNode
        pos = self.__size - 1
        if pos <= 0:
            raise ValueError("Out of bounds")
        if pos == 1:
            val = temp.data
            self.__head.nextNode = None
            self.__size = pos
            return val
        else:
            val = temp.data
            self.__head.nextNode = self.__head.nextNode.nextNode
            self.__size = pos
            return val

    
