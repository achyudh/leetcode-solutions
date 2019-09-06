class TrieNode:
    def __init__(self):
        self.childNodes = dict()
        self.isLastChar = False

class MagicDictionary:

    def __init__(self):
        self.rootNode = TrieNode()
        
    def insertWord(self, word) -> None:
        currentNode = self.rootNode       
        for char in word:
            if char not in currentNode.childNodes:
                currentNode.childNodes[char] = TrieNode()
            currentNode = currentNode.childNodes[char]    
        currentNode.isLastChar = True
    
    def searchNode(self, currentNode, word: str, index: int, changesLeft: int) -> bool:
        if index == len(word):
            return currentNode.isLastChar and not changesLeft
        
        if word[index] in currentNode.childNodes:
            childNode = currentNode.childNodes[word[index]]
            if self.searchNode(childNode, word, index + 1, changesLeft):
                return True
        
        if changesLeft > 0:
            for char, childNode in currentNode.childNodes.items():
                if char != word[index] and self.searchNode(childNode, word, index + 1, changesLeft - 1):
                    return True
        
        return False
        

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary from the given list of words
        """
        for word in dict:
            self.insertWord(word)
        

    def search(self, word: str) -> bool:
        """
        Returns True if there is a word in the dictionary 
        that is identical to the given word after modifying 
        exactly one character
        """
        return self.searchNode(self.rootNode, word, 0, 1)

