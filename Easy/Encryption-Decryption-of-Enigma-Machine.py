# https://www.codingame.com/ide/puzzle/encryptiondecryption-of-enigma-machine

import sys
import math

rotorList = []
alphabet ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
resultText = ''

operation = input()
startingShift = int(input())

# Create a rotorList that contains the 3 rotors
for i in range(3):
    rotorList.append(input())

message = input()

# Perform a Caesar shift on the message
def CaesarShift (message : str, Shift : int) :
    i=0
    text =''

    for char in message :
        if operation =='ENCODE' : 
            finalShift = alphabet.index(char)+i+Shift
            while finalShift > 25 : finalShift -= 26
        elif operation =='DECODE' : 
            finalShift = alphabet.index(char)-i-Shift
            while finalShift < -25 : finalShift += 26
        text += alphabet[finalShift]
        i+=1
    return text  

# Map the result to the 1st, 2nd and 3rd ROTOR
def rotor (message : str, rotorList : list, rotor_Number : int) :
    if operation == 'ENCODE' :
        return ''.join([rotorList[rotor_Number][alphabet.index(char)] for char in message])
    else :
        return ''.join([alphabet[rotorList[rotor_Number].index(char)] for char in message])

# Print the Encoded or Decoded String
if operation == 'ENCODE' :
    mes = CaesarShift (message, startingShift)
    rotor1 = rotor (mes, rotorList, 0)
    rotor2 = rotor (rotor1, rotorList, 1)
    resultText = rotor (rotor2, rotorList, 2)

else : # Decode

    rotor1 = rotor (message, rotorList, 2)
    rotor2 = rotor (rotor1, rotorList, 1)
    rotor3 = rotor (rotor2, rotorList, 0)
    print("rotor3", rotor3, file=sys.stderr, flush=True)
    resultText = CaesarShift (rotor3, startingShift)

print(resultText)
