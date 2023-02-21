IN PROGRESS......

instructions = 'fg9 ls11 oe7'.split()
print(instructions)

field = ['{}'*19]*25
indexX = ord(instructions[0][0])-97
indexY = ord(instructions[0][1])-97
diameter = instructions[0][2:]
print(indexX,indexY,diameter)

field[indexY] = field[indexY][:(indexX*2)] + '  ' + field[indexY][(indexX*2)+2:]
print(field)
