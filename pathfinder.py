myX, myY = 20, 19
desX, desY = 42, 15

#[x, y, FScore, GScore, px, py]
openScoreList = []

#[x,y, px, py]
closeParentList = []

#[x,y]
closeList = []
openList = []

def display(myPath, obstacleList):
	myX = myPath[0][0] 
	myY = myPath[0][1]
	desX = myPath[len(myPath) - 1][0]
	desY = myPath[len(myPath) - 1][1]

	minX, maxX, minY, maxY = None, None, None, None
	for item in myPath:
		if(minX == None or minX > item[0]):
			minX = item[0]
		if(maxX == None or maxX < item[0]):
			maxX = item[0]
		if(minY == None or minY > item[1]):
			minY = item[1]
		if(maxY == None or maxY < item[1]):
			maxY = item[1]

	for item in obstacleList:
		if(minX == None or minX > item[0]):
			minX = item[0]
		if(maxX == None or maxX < item[0]):
			maxX = item[0]
		if(minY == None or minY > item[1]):
			minY = item[1]
		if(maxY == None or maxY < item[1]):
			maxY = item[1]

	minX = min(myX,desX,minX)
	maxX = max(myX,desX,maxX)
	minY = min(myY,desY,minY)
	maxY = max(myY,desY,maxY)

	if(len(myPath) == 0):
		print "FAILURE: A path cannot be founded"
	else:
		print "SUCCESS: A path is founded"

	print ""

	width, height = maxX-minX+1, maxY-minY+1

	for r in xrange(height):
		string = ""
		for c in xrange(width):
			x = c + minX
			y = r + minY 
			if(x == myX and y == myY):
				string += "S "
			elif(x == desX and y == desY):
				string += "G "
			elif([x, y] in myPath):
				string += "x "
			elif([x, y] in obstacleList):
				string += "O "
			else:
				string +=  "  "
		print string


def getHScore(x, y):
	return abs(desX - x) + abs(desY - y)

def getGScore(lastG):
	return lastG + 1

def getFScore(x, y, lastG):
	return getHScore(x, y) + getGScore(lastG)

def getAdjacent(x, y):
	adjacentList = []
	for r in xrange(-1, 2):
		for c in xrange(-1, 2):
			if((r == 0) != (c == 0)): #this is exclusive or
				adjacentList.append([x+r, y+c])
	return adjacentList

def tracePath(x, y):
	index = closeList.index([x,y])

	px = closeParentList[index][2]
	py = closeParentList[index][3]
	#make sure this is not the beginning
	if (px != -1 or py != -1):
		myList = tracePath(px,py)
		myList.append([x,y])
		return myList
	else:
		return [[x,y]]

def findPath(x, y, gScore, desX, desY, obstacleList):
	#remove from the openList
	if([x, y] in openList):
		index = openList.index([x, y])
	

		#put it in the close list
		closeParentList.append([x, y, openScoreList[index][4], openScoreList[index][5]])
		closeList.append([x,y])

		openList.pop(index)
		openScoreList.pop(index)
	else:
		#the beginning
		closeParentList.append([x, y, -1, -1])
		closeList.append([x,y])

	#check if destination reached
	if(x == desX and y == desY):
		return tracePath(x,y)
	

	#get adjacents that are not in the close list
	for item in getAdjacent(x, y):
		#make sure it is not in the close list or has an obstacle
		if(item not in closeList and item not in obstacleList): 
			#if it is in the openList then need recalculation 
			if(item in openList):
				index = openList.index(item)

				#get the new fscore
				temp = getFScore(item[0], item[1], gScore)
				#if lower then change the Fscore and the parent
				if(openScoreList[index][2] > temp):
					openScoreList[index][2] = temp
					openScoreList[index][3] = gScore + 1
					openScoreList[index][4] = x
					openScoreList[index][5] = y
			else:
				#then just add it in with everything
				openList.append(item)
				openScoreList.append([item[0], item[1], getFScore(item[0], item[1], gScore), getGScore(gScore), x, y])		

	#now find the location in the lowest f score

	bestItem = None;

	for item in openScoreList:
		if(bestItem == None or bestItem[2] > item[2]):
			bestItem = item

	#if there is a possible path keep trying
	if(bestItem != None):
		return findPath(bestItem[0], bestItem[1], bestItem[3], desX, desY, obstacleList)
	else:
		return []

