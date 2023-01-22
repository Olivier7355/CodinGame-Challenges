w = int(input())                    # Width
h = int(input())                    # Height
CompressedFax = input().split(' ')  # Integers describing the compressed fax

CompressedFax = [int(x) for x in CompressedFax]     # Convert to integer
decompressed =[]

for i in range(len(CompressedFax)) :
    if i%2 == 0 : decompressed += CompressedFax[i] * '*'
    else : decompressed += CompressedFax[i] * ' '

print('|', end='')
for char in range(len(decompressed)) :
    if (char%w == 0) and (char > 0) :print('|\n|', end='')
    print(decompressed[char], end='')
print('|')
