# https://www.codingame.com/ide/puzzle/rectangle-partition

sizeSegmentx = []
sizeSegmenty = []

numberSquares = 0
smalestSize = None
largestSize = None

w, h, count_x, count_y = [int(i) for i in input().split()]

xMeasureList = input().split()
xMeasureList = [int(x) for x in xMeasureList]

yMeasureList = input().split()
yMeasureList = [int(x) for x in yMeasureList]

xMeasureList.insert(0,0)
xMeasureList.append(w)
xMeasureList.reverse()

yMeasureList.insert(0,0)
yMeasureList.append(h)
yMeasureList.reverse()

beginList = 0
endList = len(xMeasureList)-1
while beginList < endList :
    for i in range(beginList+1, endList+1) :
        sizeSegmentx.append(xMeasureList[beginList] - xMeasureList[i])
    beginList +=1

beginList = 0
endList = len(yMeasureList)-1
while beginList < endList :
    for i in range(beginList+1, endList+1) :
        sizeSegmenty.append(yMeasureList[beginList] - yMeasureList[i])
    beginList +=1

if (sizeSegmentx > sizeSegmenty) : 
    smalestSize = sizeSegmenty
    largestSize = sizeSegmentx
else :
    smalestSize = sizeSegmentx
    largestSize = sizeSegmenty

for i in range(len(smalestSize)) :
    numberSquares += largestSize.count(smalestSize[i])

print(numberSquares)
