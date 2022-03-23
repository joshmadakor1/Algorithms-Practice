'''
    Populate Suffix Trie:
    Populate a suffix trie given a string
    Implement a function that returns a boolean based on whether or not the
    suffix trie contains the input string

    Creation:
    ---------
    Time:  O(N^2) - Exponential 
    Space: O(N^2) - Linear (Alternate O(D), where D is the depth of the suffix trie)

    Searching:
    ----------
    Time: O(N) - Linear
    Space: O(1) - Constant

    Last Practiced: 2022-03-23 06:46:51
'''
# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insertCharacterAtIndex(i, string)
    
    def insertCharacterAtIndex(self, index, string):
        currentNode = self.root
        for i in range(index,len(string)):
            currentChar = string[i]
            if currentChar not in currentNode:
                currentNode[currentChar] = {}
            currentNode = currentNode[currentChar]
        currentNode[self.endSymbol] = True

    def contains(self, string):
        currentNode = self.root
        for char in string:
            if char not in currentNode:
                return False
            currentNode = currentNode[char]
        return self.endSymbol in currentNode
            
