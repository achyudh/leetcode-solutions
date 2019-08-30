class TrieNode:
    def __init__(self):
        self.childNodes = dict()
        self.isLastChar = False

class Trie:
    def __init__(self):
        self.rootNode = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        currentNode = self.rootNode
        
        for char in word:
            if char not in currentNode.childNodes:
                currentNode.childNodes[char] = TrieNode()
            currentNode = currentNode.childNodes[char]
        
        currentNode.isLastChar = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        currentNode = self.rootNode
        
        for char in word:
            if char not in currentNode.childNodes:
                return False
            currentNode = currentNode.childNodes[char]
        
        return currentNode.isLastChar

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        currentNode = self.rootNode
        
        for char in prefix:
            if char not in currentNode.childNodes:
                return False
            currentNode = currentNode.childNodes[char]
            
        return True
