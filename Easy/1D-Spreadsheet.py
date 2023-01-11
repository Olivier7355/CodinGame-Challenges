# https://www.codingame.com/ide/puzzle/1d-spreadsheet

import sys
import math

cellsList =[]
operation = {"ADD": (lambda x, y: x + y),
             "SUB": (lambda x, y: x - y),
             "MULT": (lambda x, y: x * y),
             "VALUE":( lambda x, y: x)
            }

n = int(input())

# Store each line in a list of arrays (cells)
for i in range(n):
    cell=[]
    op, arg_1, arg_2 = input().split()
    cell.append(op)
    cell.append(arg_1)
    cell.append(arg_2)

    cellsList.append(cell)

# Function that convert the arg1 and arg2 to integer
def s2int(cellsList, s):
    if s == "_":
        return '_'
    if "$" not in s:
        return int(s)
    else:
        return computeCell(cellsList, int(s[1:]))

V=[None]*n

# Main function that calculates the values
def computeCell(cellsList, i):
    if V[i] is not None:
        return V[i]
    op, arg1, arg2 = cellsList[i]
    x = s2int(cellsList, arg1)
    y = s2int(cellsList, arg2)
    V[i] = operation[op](x, y)
    return V[i]

# Iterate through the list of cells and calculate each value 
for i in range(n):
    print(computeCell(cellsList,i))
