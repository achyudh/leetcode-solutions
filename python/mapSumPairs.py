class TrieNode:
    def __init__(self):
        self.childNodes = dict()
        self.isLastNode = False
        self.prefixSum = 0

        
class MapSum:
    def __init__(self):
        self.rootNode = TrieNode()
        self.values = dict()
        
    def insert(self, key: str, val: int) -> None:
        currentNode = self.rootNode
        prevVal = self.values[key] if key in self.values else 0
        
        currentNode.prefixSum += (val - prevVal)

        for char in key:
            if char not in currentNode.childNodes:
                currentNode.childNodes[char] = TrieNode()
            currentNode = currentNode.childNodes[char]
            currentNode.prefixSum += (val - prevVal)
        
        self.values[key] = val

    def sum(self, prefix: str) -> int:
        currentNode = self.rootNode
        for char in prefix:
            if char not in currentNode.childNodes:
                return 0
            currentNode = currentNode.childNodes[char]
        return currentNode.prefixSum
