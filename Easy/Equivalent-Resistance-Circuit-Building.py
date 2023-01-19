import sys
import math

ComponentDict = {}
firstIndice = None
lastIndice = None
sum = 0

n = int(input()) # Number of unique resistors
for i in range(n):
    inputs = input().split()

    # Store the components name and value in a dictionnary
    ComponentDict[inputs[0]] = int(inputs[1])

circuitList = list(input().split())

# Replace the resistors name by their value
circuitList = [ ComponentDict[char] if char in ComponentDict else char for char in circuitList ]
circuitList = [ float(char) if type(char) == int else char for char in circuitList ]

while ('(' in circuitList) or ('[' in circuitList) :

# search for '(' :    
    for i in range(len(circuitList)) :
        
        if circuitList[i] == '(' :
            firstIndice = i     
            sum = 0
        
        #As long as the next char is a number : sum += number
        elif (firstIndice != None) and (type(circuitList[i]) == float) :
            sum += circuitList[i]
        
        #if the next char is ')' : 
        elif circuitList[i] == ')' :
            LastIndice = i     # indice of ')'
            del circuitList[firstIndice : LastIndice+1]
            circuitList.insert(firstIndice, sum)
            sum = 0
            LastIndice = None
            firstIndice = None
            break
    
    for i in range(len(circuitList)) :
        
        if circuitList[i] == '[' :
            firstIndice = i     # indice of '['
            sum = 0
        
        #As long as the next char is a number : sum += number
        elif (firstIndice != None) and (type(circuitList[i]) == float) :
            sum += 1 / circuitList[i]
        
        #if the next char is ']' : 
        elif (circuitList[i] == ']') and (firstIndice != None) :
            LastIndice = i     # indice of ')'
            del circuitList[firstIndice : LastIndice+1]
            circuitList.insert(firstIndice, round(1/sum, 1))
            sum = 0
            LastIndice = None
            firstIndice = None
            break
        
        else :
            sum = 0
            LastIndice = None
            firstIndice = None
            
print(circuitList[0])
