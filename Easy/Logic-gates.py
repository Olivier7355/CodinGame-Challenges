import sys
import math

inpuDict = {}
logicList= []

n = int(input()) # Number of input signals
m = int(input()) # Number of output signals

# Store each signal in an inpuDict 
for i in range(n):
    port, inputSignal = input().split()
    inpuDict[port] = inputSignal

# Store each logic in a logicList 
for i in range(m):
    logicList.append(input().split())

# Scan each logic operation in the logicList
for i in range(m):
    output = logicList[i][0] + ' ' 

    # Compare the 2 input signals and print the result
    for cnt in range(len(inpuDict[logicList[i][2]])) :

        if logicList[i][1] == 'AND' :
            if (inpuDict[logicList[i][2]][cnt] == '-') and (inpuDict[logicList[i][3]][cnt] == '-'):
                output += '-'
            else : output += '_' 

        elif logicList[i][1] == 'NAND' :
            if (inpuDict[logicList[i][2]][cnt] == '-') and (inpuDict[logicList[i][3]][cnt] == '-'):
                output += '_'
            else : output += '-' 

        elif logicList[i][1] == 'OR' :
            if (inpuDict[logicList[i][2]][cnt] == '-') or (inpuDict[logicList[i][3]][cnt] == '-'):
                output += '-'
            else : output += '_' 

        elif logicList[i][1] == 'NOR' :
            if (inpuDict[logicList[i][2]][cnt] == '-') or (inpuDict[logicList[i][3]][cnt] == '-'):
                output += '_'
            else : output += '-' 

        elif logicList[i][1] == 'XOR' :
            if (inpuDict[logicList[i][2]][cnt] == '-') or (inpuDict[logicList[i][3]][cnt] == '-'):
                if (inpuDict[logicList[i][2]][cnt] != inpuDict[logicList[i][3]][cnt]):
                    output += '-'
                else : output += '_' 
            else : output += '_' 

        elif logicList[i][1] == 'NXOR' :
            if (inpuDict[logicList[i][2]][cnt] == '-') or (inpuDict[logicList[i][3]][cnt] == '-'):
                if (inpuDict[logicList[i][2]][cnt] != inpuDict[logicList[i][3]][cnt]):
                    output += '_'
                else : output += '-' 
            else : output += '-' 

    print(output)
