# This program finds all the degree sequences of n vertices tree.

def leaves(degree, l):
    for i in range(degree):
        l.append(1)

def unlabeledTrees(vertices):
    
    numberOfEdges = vertices - 1
    
    degreeRange = range(2,numberOfEdges + 1)
    
    degreeSequence = []
    
    for highestDegree in degreeRange:
        
        degreeSequence.append(highestDegree)

        degreeSum = 2*(numberOfEdges)
        
        k = 2*(highestDegree)
        
        degreeSum -= k
        
        if(degreeSum != 0):
            unknownVertices = vertices - (highestDegree + 1)
        
            remainingDeg = degreeSum // unknownVertices
            
            for i in range(unknownVertices):
                degreeSequence.append(remainingDeg)
        
        leaves(highestDegree,degreeSequence)
        
        subset_sum(range(1,highestDegree), degreeSum)
        
        print degreeSequence
        
        degreeSequence[:] = []
        
def subset_sum(numbers, target, partial=[]):
    s = sum(partial)
    
    # check if the partial sum is equals to target
    if s == target: 
        print partial
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n]) 
      
unlabeledTrees(7)
