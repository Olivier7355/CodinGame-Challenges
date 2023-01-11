# https://www.codingame.com/ide/puzzle/1d-spreadsheet
# Fail Test case 13 : Deep Birecursion
# Error : Process has timed out. This may mean that 
#         your solution is not optimized enough to handle some cases.

import sys
import math

cellsList =[]

# Each operation is assigned to a function that makes the calculation
operation = {'ADD'  :lambda x,y:int(x)+int(y),
             'SUB'  :lambda x,y:int(x)-int(y),
             'MULT' :lambda x,y:int(x)*int(y),
             'VALUE':lambda x,y:int(x)}

# The function that calculate the values
def computeCell(i) :
    op, arg1, arg2 = cellsList[i]
    if '$' in arg1 : arg1 = computeCell(int(arg1[1:]))
    if '$' in arg2 : arg2 = computeCell(int(arg2[1:]))
    return op(arg1,arg2)

n = int(input())

# Store each line in a list of arrays (cells)
for i in range(n):
    cell=[]
    op, arg_1, arg_2 = input().split()
    cell.append(operation[op])
    cell.append(arg_1)
    cell.append(arg_2)

    cellsList.append(cell)

# Call the funtion for each cell
for i in range(n):
    print(computeCell(i))
