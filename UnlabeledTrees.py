
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

        degreeSum = 2*(numberOfEdges)
        
        k = 2*(highestDegree)
        
        degreeSum -= k
        
        if(degreeSum != 0):
            unknownVertices = vertices - (highestDegree + 1)
        
            remainingDeg = degreeSum // unknownVertices
            
            for i in range(unknownVertices + 1):
                degreeSequence.append(remainingDeg)
        
        leaves(highestDegree,degreeSequence)
        print degreeSequence
        
        degreeSequence[:] = []

        
unlabeledTrees(6)
        
