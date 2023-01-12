import sys
import math

l = int(input())
h = int(input())
t = input()

row = []
alphabet =['A','B','C','D','E','F','G','H','I','J','K',
            'L','M','N','O','P','Q','R','S','T','U','V',
            'W','X','Y','Z','?']

for i in range(h) :
    ligne = input()
    row.append(ligne)

t = list(t.upper())

for char in range(len(t)):
    if t[char].isalpha() == False : 
        t[char] = '?'

for i in range(len(row)) :
    line=''
    for char in t :
        indice = alphabet.index(char)
        line += row[i][(indice*l) : (indice*l)+l]
    print(line)
