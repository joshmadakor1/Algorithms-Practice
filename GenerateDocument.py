'''
    Generate Document:
    Given an array of characters and a target document, determine if the
    character array has the necessary characters (including count), to
    create the document

    Time: O(C + D) -> O(N), where C=characters and D=document
    Space: O(C) -> O(N), where N is the size of the character dictionary

    Last Practiced: 2022-03-10 07:59:34
'''
def generateDocument(characters, document):
    chars = {}
    for character in characters:
        if character not in chars:
            chars[character] = 0
        chars[character] += 1
    
    for character in document:
        if character not in chars or chars[character] == 0:
            return False
        chars[character] -= 1
    
    return True