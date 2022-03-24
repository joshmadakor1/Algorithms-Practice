
'''
	Youngest Common Ancestor:
	Given a family tree, top ancestor, and two descendants at different levels,
	find the youngest common ancestor between the two descendants

	Time:  O(N) - Linear (Alternate O(D), where D is the depth of the family tree)
	Space: O(1) - Constant

	Last Practiced: 2022-03-24 09:31:42
'''
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
	
	# calculate the distance from each descendant to the top ancestor
	distanceOne = getDistanceFromYoungestAncestor(descendantOne, topAncestor)
	distanceTwo = getDistanceFromYoungestAncestor(descendantTwo, topAncestor)
	
	# travel up each branch until both descendants are at the same level
	descendantOne, descendantTwo = moveDescendantsToSameLevel(distanceOne, distanceTwo, descendantOne, descendantTwo)
	
	# if They are in the same family tree, the "younger" person will
	# be the youngest common ancestor
	if descendantOne == descendantTwo:
		return descendantOne
	
	# now that they are on the same level, both descendants will
	# travel up the family tree until they have the same ancestor
	while descendantOne.ancestor != descendantTwo.ancestor:
		descendantOne = descendantOne.ancestor
		descendantTwo = descendantTwo.ancestor
	
	# return the youngest common ancestor
	return descendantOne.ancestor

# calculates the distances from a descendant to the top ancestor
def getDistanceFromYoungestAncestor(descendant, topAncestor):
	distance, travelNode = 0, descendant
	while travelNode.ancestor is not None:
		distance += 1
		travelNode = travelNode.ancestor
	return distance

# given each descendants distance from the top ancestor, moves
# the lower descendant up the family tree until both descendants
# are on the same level
def moveDescendantsToSameLevel(distanceOne, distanceTwo, descendantOne, descendantTwo):
	while distanceOne != distanceTwo:
		if distanceOne < distanceTwo:
			descendantTwo = descendantTwo.ancestor
			distanceTwo -= 1
		elif distanceTwo < distanceOne:
			descendantOne = descendantOne.ancestor
			distanceOne -= 1
	return [descendantOne, descendantTwo]

	'''
	Other Implementation:
	# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    distance1 = getDistanceFromYoungestCommonAncestor(descendantOne, topAncestor)
    distance2 = getDistanceFromYoungestCommonAncestor(descendantTwo, topAncestor)
	descendantOne, descendantTwo = moveDescendantsToSameLevel(descendantOne, descendantTwo, distance1, distance2)
	if descendantOne == descendantTwo: return descendantOne
	while descendantOne.ancestor != descendantTwo.ancestor:
		descendantOne = descendantOne.ancestor
		descendantTwo = descendantTwo.ancestor
	return descendantOne.ancestor

def getDistanceFromYoungestCommonAncestor(descendant, topAncestor):
	travelNode = descendant
	distance = 0
	while travelNode.ancestor is not None:
		travelNode = travelNode.ancestor
		distance += 1
	return distance

def moveDescendantsToSameLevel(descendantOne, descendantTwo, distance1, distance2):
	while distance1 != distance2:
		if distance1 > distance2:
			descendantOne = descendantOne.ancestor
			distance1 -= 1
		else:
			descendantTwo = descendantTwo.ancestor
			distance2 -= 1
	return descendantOne, descendantTwo
			
	'''