import sys
import math

# Create a dict recipeList that contains the corespondances abbreviation/char
recipeList ={'sp':' ', 
             'bS':'\\', 
             'sQ': "'", 
             'nl' : '\n'
             }

# split the input and store the chunk in a recipe list
recipe = input().split()

# Check each Chunck in the recipe :
for i in range(len(recipe)): 

    # If a chunk is composed only of numbers, the character is the last digit
    if recipe[i].isnumeric() : print(recipe[i][-1] * int(recipe[i][0:-1]), end='')

    # Elif the 2 last characters is in dict recipeList, the characters are an abbreviation
    elif recipe[i][-2:] in recipeList :
        if recipeList[recipe[i][-2:]] =='\n' :
            cnt = 1
        else : cnt = int(recipe[i][0:-2])
        
        print(recipeList[recipe[i][-2:]] * cnt, end='')
        #print("cnt", cnt, file=sys.stderr, flush=True)
    
    # Else the last character is the character to display
    else : print(recipe[i][-1] * int(recipe[i][0:-1]), end='')
