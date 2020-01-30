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
    
    def pop(self):
        if self.__size == 0:
            return ValueError("Buffer empty")
        elif self.__size == 1:
            self.__size = 0
            self.__head = None
        temp = self.__head.data
        self.__head = self.__head.nextNode
        self.__size -= 1
        return temp
    
    def pop_front(self):
        if self.__size == 0:
            return ValueError("Buffer empty")
        elif self.__size == 1:
            self.__size = 0
            self.__head = None
        self.__size -= 1
        temp = self.__head
        while temp.nextNode is not None:
            temp = temp.nextNode
        val = temp.nextNode.data
        temp.nextNode = None
        return val
    
    def __len__(self):
        return self.__size
    
    def __iter__(self):
        temp = self.__head
        while temp is not None:
            yield temp.data
            temp = temp.nextNode
    
    def __str__(self):
        out = "["
        temp = self.__head
        for i in range(self.__size):
            out += str(temp.data)
            if i < self.__size - 1: out += ", "
            temp = temp.nextNode
        out += "]"
        return out
    
    def clear(self):
        self.__size = 0
        self.__head = None
    
    def resize(self, value, default = None):
        if value <= 0:
            raise ValueError("Negative or zero resize value")
        self.__head = Node(default)
        self.__size = value
        temp = self.__head
        for i in range(1, value):
            temp.nextNode = Node(default)
            temp = temp.nextNode

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

    def first(self):
        if self.__size == 0:
            raise ValueError("Buffer empty")
        return self.__head.data
    
    def last(self):
        if self.__size == 0:
            raise ValueError("Buffer empty")
        temp = None
        for x in self:
            temp = x
        return temp

    def popAt(self, i):
        if i < 0 or i >= self.__size:
            raise IndexError("Out of bounds")
        if i == 0: 
            temp = self.__head.data
            self.__head = self.__head.nextNode
            self.__size -= 1
            return temp
        elif i == self.__size - 1:
            return self.pop_front()
        else:
            temp = self.__head
            for _ in range(i - 1):
                temp = temp.nextNode
            val = temp.nextNode.data
            temp.nextNode = temp.nextNode.nextNode
            self.__size -= 1
            return val