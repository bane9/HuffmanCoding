from HuffmanCoding import HuffmanCoding

hCoding = HuffmanCoding()

with open("data/original.txt", "r") as F:
    data = F.read()

compressed = hCoding.compress(data)

with open("data/compressed.bin", "wb") as F:
    F.write(compressed)

decoded = hCoding.decode(compressed)

with open("data/decoded.txt", "w") as F:
    F.write(decoded)
