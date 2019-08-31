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
        
    def getRoot(self, word: str) -> str:
        """
        Returns the root corresponding to a word.
        """
        rootWord = list()
        currentNode = self.rootNode
        
        for char in word:
            if currentNode.isLastChar:
                return ''.join(rootWord)
            
            elif char not in currentNode.childNodes:
                return word
            
            else:
                rootWord.append(char)
                currentNode = currentNode.childNodes[char]
        
        return word

class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        trieDict = Trie()
        rootSentence = list()
        
        for word in dict:
            trieDict.insert(word)
        
        return ' '.join(trieDict.getRoot(word) for word in sentence.split())
