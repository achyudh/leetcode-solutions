class TrieNode:
    def __init__(self):
        self.childNodes = [None for _ in range(26)]
        self.isLastChar = False
    
class Trie:
    def __init__(self):
        self.rootNode = TrieNode()
    
    def insert(self, word):
        currentNode = self.rootNode
        for char in word:
            nextIndex = ord(char) - ord('a')
            if not currentNode.childNodes[nextIndex]:
                currentNode.childNodes[nextIndex] = TrieNode()
            currentNode = currentNode.childNodes[nextIndex]
        currentNode.isLastChar = True
        
    
class Solution:
    def getLongestWord(self, currentNode):
        longestWord = ''

        for i0 in range(len(currentNode.childNodes)):
            childNode = currentNode.childNodes[i0]
            if childNode and childNode.isLastChar:
                currentWord = chr(ord('a') + i0) + self.getLongestWord(childNode)
                if len(currentWord) > len(longestWord):
                    longestWord = currentWord

        return longestWord

    def longestWord(self, words: List[str]) -> str:
        dictionary = Trie()
        for word in words:
            dictionary.insert(word)
            
        return self.getLongestWord(dictionary.rootNode)
