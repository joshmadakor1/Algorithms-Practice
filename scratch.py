# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    descendantOneDistanceFromTop = getDistanceFromDescendantToTopAncestor(topAncestor, descendantOne)
    descendantTwoDistanceFromTop = getDistanceFromDescendantToTopAncestor(topAncestor, descendantTwo)
    
    # Bring them to the same level
    while descendantOneDistanceFromTop != descendantTwoDistanceFromTop:
        if descendantOneDistanceFromTop > descendantTwoDistanceFromTop:
            descendantOne = descendantOne.ancestor
            descendantOneDistanceFromTop -= 1
        else:
            descendantTwo = descendantTwo.ancestor
            descendantTwoDistanceFromTop -= 1
    
    # If they were in the same branch:
    if descendantOne == descendantTwo:
        return descendantOne
    
    # Keep climbing until they have the same ancestor or until they are the same
    while descendantOne is not None:
        if descendantOne.ancestor == descendantTwo.ancestor:
            return descendantOne.ancestor
        descendantOne = descendantOne.ancestor
        descendantTwo = descendantTwo.ancestor
        
    return None # This means there is no common ancestor. Impossible to happen
            
    

def getDistanceFromDescendantToTopAncestor(topAncestor, descendant):
    distance = 0
    while descendant != topAncestor:
        distance += 1
        descendant = descendant.ancestor
    return distance

    
