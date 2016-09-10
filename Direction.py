from pathfinder import findPath, display

myX, myY = 20, 19
desX, desY = 42, 15

obstacleList = [[1,3]]

def findDirection(myPath, tDirection):
	#0 = forward -1 = left 1 = right
	myDirection = []

	#0 = N 1 = E 2 = S 3 = W for the direction
	direction = tDirection

	previousNode = []
	for x in myPath:
		if(myPath.index(x) == 0):
			previousNode = x
		else:
			smallDirection = []

			newDirection = getDirectionNSWE(previousNode, x)			

			#add the turn
			diff = newDirection - direction
			if(abs(diff) == 3):
				diff /= -3

			if(abs(diff) == 2):
				smallDirection.append(1)
				smallDirection.append(1)
			elif(diff != 0):
				smallDirection.append(diff)


			#move forward
			smallDirection.append(0)

			myDirection.append(smallDirection)
			direction = newDirection
			previousNode = x

	return myDirection

def getDirectionNSWE(prev, next):
	#Move East
			if(prev[0] - next[0] == -1):
				return 1
			#Move West
			elif(prev[0] - next[0] == 1):
				return 3
			#Move South
			elif(prev[1] - next[1] == -1):
				return 2
			#Move North
			elif(prev[1] - next[1] == 1):
				return 0
			else:
				pass

def getSolution(myX, myY, desX, desY, myDir, obstacleList):
	myPath = findPath(myX, myY, myDir, desX, desY, obstacleList)
	direction = findDirection(myPath, 1)
	display(myPath, obstacleList)
	return [myPath, direction]

#print getSolution(2, 3, 8, 10, 0, [[2,5],[9,2]])