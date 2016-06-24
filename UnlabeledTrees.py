
def leaves(degree, l):
    for i in range(degree):
        l.append(1)

def unlabeledTrees(vertices):
    
    numberOfEdges = vertices - 1
    
    degreeRange = range(1,numberOfEdges + 1)
    
    degreeSequence = []
    
    listOfSequences = []
    
    for highestDegree in degreeRange:
        
        degreeSequence.append(highestDegree)
        
        leaves(highestDegree,degreeSequence)

        degreeSum = 2*(numberOfEdges)
        
        k = 2*(highestDegree)
        
        degreeSum -= k
        
        unknownVertices = vertices - (highestDegree - 1)
        
        print degreeSequence
        
        degreeSequence[:] = []
 
unlabeledTrees(7)
        
