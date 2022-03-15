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

    Last Practiced: 2022-03-15 07:20:02
'''
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for index in range(len(string)):
            self.insertStringFrom(string, index)
    
    def insertStringFrom(self, string, index):
        currentNode = self.root
        for i in range(index, len(string)):
            if string[i] not in currentNode:
                currentNode[string[i]] = {}
            currentNode = currentNode[string[i]]
        currentNode[self.endSymbol] = True

    def contains(self, string):
        currentNode = self.root
        for char in string:
            if char not in currentNode:
                return False
            currentNode = currentNode[char]
        return self.endSymbol in currentNode
