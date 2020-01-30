from Tree.MinHeap import MinHeap
import heapq

class HeapNode:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq
    
class HuffmanCoding:
    def __init__(self):
        self.__heap = []
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
            heapq.heappush(self.__heap, HeapNode(k, v))

        while(len(self.__heap) > 1):
            node1 = heapq.heappop(self.__heap)
            node2 = heapq.heappop(self.__heap)

            merged = HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.__heap, merged)
    
        root = heapq.heappop(self.__heap)
        self.__makeCodes(root, "")

    def __makeCodes(self, root, currentNode):
        if root is None: return

        if root.data is not None:
            self.__codes[root.data] = currentNode
            self.__reverseMapping[currentNode] = root.data
            return
        
        self.__makeCodes(root.left, currentNode + "0")
        self.__makeCodes(root.right, currentNode + "1")

    
    def __generateBinary(self, text):
        encoded = ""

        for x in text:
            encoded += self.__codes[x]
        
        padding = 8 - len(encoded) % 8
        for _ in range(padding):
            encoded += "0"

        padded = "{0:08b}".format(padding)
        encoded = padded + encoded

        out = bytearray()
        for i in range(0, len(encoded), 8):
            byte = encoded[i:i+8]
            out.append(int(byte, 2))
        return out

    def compress(self, text):
        self.__processTree(text)
        return self.__generateBinary(text)

    def decode(self, bytearr):
        out = ""
        for x in bytearr:
            out += bin(x)[2:].rjust(8, '0')
        
        padded = out[:8]
        additionalPadding = int(padded, 2)

        out = out[8:] 
        out = out[:-1 * additionalPadding]

        buff = ""
        decoded = ""

        for x in out:
            buff += x
            if(buff in self.__reverseMapping):
                c = self.__reverseMapping[buff]
                decoded += c
                buff = ""

        return decoded
