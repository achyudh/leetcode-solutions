class Node:
    def __init__(self):
        self.childNodes = dict()
        self.isLastChar = False

class WordDictionary:
    def __init__(self):
        self.rootNode = Node()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        currentNode = self.rootNode  
        
        for char in word:
            if char not in currentNode.childNodes:
                currentNode.childNodes[char] = Node()
            currentNode = currentNode.childNodes[char]
            
        currentNode.isLastChar = True
        
    def searchNode(self, currentNode: Node, word: str, index: int) -> Node:
        if index == len(word):
            return currentNode.isLastChar
        
        elif word[index] == '.':
            for childNode in currentNode.childNodes.values():    
                if self.searchNode(childNode, word, index + 1):
                    return True
                
        elif word[index] in currentNode.childNodes:
            return self.searchNode(currentNode.childNodes[word[index]], word, index + 1)
        
        return False

    def search(self, word: str) -> bool:
        """
        Returns if the word or regex is in the data structure.
        """
        return self.searchNode(self.rootNode, word, 0)

