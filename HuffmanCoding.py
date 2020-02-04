from Tree.MinHeap import MinHeap

class HeapNode:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        if not isinstance(other, HeapNode): return False
        else: return self.freq < other.freq
    
class HuffmanCoding:
    def __init__(self):
        self.__heap = MinHeap()
        self.__codes = {}
        self.__reverseMapping = {}

    def __processTree(self, data):
        self.__heap.clear()
        self.__codes.clear()
        self.__reverseMapping.clear()
        
        freq = {}
        for x in data:
            freq[x] = freq.get(x, 0) + 1
        
        for k, v in freq.items():
            self.__heap.insert(HeapNode(k, v))

        while(len(self.__heap) - 1 > 1):
            node1 = self.__heap.pop()
            node2 = self.__heap.pop()

            merged = HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            self.__heap.insert(merged)

        self.__makeCodes(self.__heap.pop(), "")

    def __makeCodes(self, node, currentNode):
        if node is None: return

        if node.data is not None:
            self.__codes[node.data] = currentNode
            self.__reverseMapping[currentNode] = node.data
            return
        
        self.__makeCodes(node.left, currentNode + "0")
        self.__makeCodes(node.right, currentNode + "1")


    def __generateBinary(self, text):
        encoded = ""

        for x in text:
            encoded += self.__codes[x]
        
        padding = 8 - len(encoded) % 8
        for _ in range(padding):
            encoded += "0"

        encoded = "{0:08b}".format(padding) + encoded

        out = bytearray()
        for i in range(0, len(encoded), 8):
            out.append(int(encoded[i:i+8], 2))
        return out

    def compress(self, text):
        self.__processTree(text)
        return self.__generateBinary(text)

    def decode(self, bytearr):
        out = ""
        for x in bytearr:
            out += bin(x)[2:].rjust(8, '0')

        out = out[8:-1 * int(out[:8], 2)]

        buff = ""
        decoded = ""

        for x in out:
            buff += x
            if(buff in self.__reverseMapping):
                decoded += self.__reverseMapping[buff]
                buff = ""

        return decoded
