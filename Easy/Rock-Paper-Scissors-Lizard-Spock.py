tournamentList = []

n = int(input())
for i in range(n):
    inputs = input().split()
    tournamentList.append(inputs)
    
# Dict letterSign with corespondance between letter and sign
letterSign = {'R' : 'Rock',
              'P' : 'Paper',
              'C' : 'Scissors',
              'L' : 'Lizard',
              'S' : 'Spock'
             }

# Create winningPosistionsv dict with winning positions
winningPosistions = {'Scissors' : ['Paper', 'Lizard'],
                     'Paper' : ['Rock', 'Spock'],
                     'Rock' : ['Lizard', 'Scissors'],
                     'Lizard': ['Spock', 'Paper'],
                     'Spock' : ['Scissors', 'Rock']
                    }

# Dict historyList that will contain each players and the history of his adversaries
historyList = [[]]*(n+1)
tempList = []

# Repat the process until tournamentList =1 :
while len(tournamentList ) > 1 :
    tempList = []

    # For each player in the tournamentList :
    for i in range(0,len(tournamentList)-1,2) :
    
        # Check the winner of 2 consecutive players in the list
        if letterSign[tournamentList[i][1]] in winningPosistions[letterSign[tournamentList[i+1][1]]] :
            tempList.append(tournamentList[i+1])
            historyList[int(tournamentList[i+1][0])] = historyList[int(tournamentList[i+1][0])][ : ] + [tournamentList[i][0]]
            
        elif letterSign[tournamentList[i+1][1]] in winningPosistions[letterSign[tournamentList[i][1]]] :
            tempList.append(tournamentList[i])
            historyList[int(tournamentList[i][0])] = historyList[int(tournamentList[i][0])][ : ] + [tournamentList[i+1][0]]
            
        elif letterSign[tournamentList[i+1][1]] == letterSign[tournamentList[i][1]] :
            if int(tournamentList[i][0]) < int(tournamentList[i+1][0]) : 
                tempList.append(tournamentList[i])
                historyList[int(tournamentList[i][0])] = historyList[int(tournamentList[i][0])][ : ] + [tournamentList[i+1][0]]
            else : 
                tempList.append(tournamentList[i+1])
                historyList[int(tournamentList[i+1][0])] = historyList[int(tournamentList[i+1][0])][ : ] + [tournamentList[i][0]]
    
    tournamentList = tempList[ : ]     
print(tournamentList[0][0])
print(' '.join(historyList[int(tournamentList[0][0])]))
