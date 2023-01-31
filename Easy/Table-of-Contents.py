# https://www.codingame.com/ide/puzzle/table-of-contents
  
import sys
import math

titleList = []
titles = [0]*10

lengthofline = int(input())
n = int(input())
for i in range(n):
    entry = input().split(' ')
    titleList.append(entry)

# For each line in titleList :
for i in range(len(titleList)) :
    tabelOfContent = ''
    titre =''

    # Count number of '>' in titleList[i][0]
    counter = titleList[i][0].count('>')
    for j in range(titles[counter+1], len(titles)) :
        titles[counter+1] = 0

    # If there is n number of '>' then inc titles[n]
    titles[counter] += 1

    # For each '>' add 4 * ' ' to the tabelOfContent line
    tabelOfContent += counter * '    '

    # Add titles[n] + ' ' to the tabelOfContent line
    tabelOfContent += str(titles[counter]) + ' '

    # Remove all '>' in titleList[i][0] and add the result to the tabelOfContent line
    for char in titleList[i][0] :
        if char !='>' : titre += char
    tabelOfContent += titre 

    # Add lengthofline - len(tabelOfContent) - len(titleList[i][1]) * '.' after the title
    tabelOfContent += (lengthofline - len(tabelOfContent) - len(titleList[i][1])) * '.'

    # Add titleList[i][1] (page number)
    tabelOfContent += titleList[i][1]

    print(tabelOfContent)

