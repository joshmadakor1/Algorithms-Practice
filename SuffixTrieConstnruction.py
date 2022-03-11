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

    Last Practiced: 2022-03-11 11:07:24
'''
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.popualateSuffixTrieFrom(string)

    def popualateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insertStringAtIndex(i, string)

    def insertStringAtIndex(self, index, string):
        node = self.root
        for i in range(index,len(string)):
            character = string[i]
            if character not in node:
                node[character] = {}
            node = node[character]
        node[self.endSymbol] = True

    def contains(self, string):
        node = self.root
        for character in string:
            if character not in node:
                return False
            node = node[character]
        return self.endSymbol in node
