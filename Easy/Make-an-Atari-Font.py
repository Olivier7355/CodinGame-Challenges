# https://www.codingame.com/ide/puzzle/make-an-atari-font

import sys
import math

wordList = []
bufferArray = [[] for i in range(15)]

# Dictionary containing the alphabet
dictAlphabet ={ 'A' : '0x1818243C42420000', 'B' : '0x7844784444780000', 
                'C' : '0x3844808044380000', 'D' : '0x7844444444780000', 
                'E' : '0x7C407840407C0000', 'F' : '0x7C40784040400000', 
                'G' : '0x3844809C44380000', 'H' : '0x42427E4242420000', 
                'I' : '0x3E080808083E0000', 'J' : '0x1C04040444380000', 
                'K' : '0x4448507048440000', 'L' : '0x40404040407E0000', 
                'M' : '0x4163554941410000', 'N' : '0x4262524A46420000', 
                'O' : '0x1C222222221C0000', 'P' : '0x7844784040400000', 
                'Q' : '0x1C222222221C0200', 'R' : '0x7844785048440000', 
                'S' : '0x1C22100C221C0000', 'T' : '0x7F08080808080000', 
                'U' : '0x42424242423C0000', 'V' : '0x8142422424180000', 
                'W' : '0x4141495563410000', 'X' : '0x4224181824420000', 
                'Y' : '0x4122140808080000', 'Z' : '0x7E040810207E0000'
            }

wordList = list(input().upper())
cpt = 0

# For each letter in wordList :
for letter in wordList :

    # Convert the Hex Value into a 64 bit-long Binary Value
    hexValue = dictAlphabet[letter][2:]
    binValue = bin(int(hexValue, 16))[2:]
    
    binValue = '0'* (64 - len(binValue)) + binValue
    binValue = binValue[ : -8]
    binValue = binValue.replace("1", "X" )
    binValue = binValue.replace("0", " " )
    
    # Split that Binary Value into 8 different lines
    for i in range(0, 64, 8) :
        
        # Append the lines in bufferArray
        bufferArray[cpt].append(binValue[i:i+8])
    
    cpt +=1
    
for i in range(8) :
    bufferArray[len(wordList)-1][i] = bufferArray[len(wordList)-1][i].rstrip()

# Display the content of bufferArray
# For each line in bufferArray :
for j in range(6) :
    for i in range(len(wordList)) :
        print(bufferArray[i][j], end='')
    print()
