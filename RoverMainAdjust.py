from Direction import getSolution, getDirectionNSWE

gridSize = 1

obstacleList = []

myX = 0
myY = 0
myDir = 1


forward = 5#input('How many meters do you want to go forward: ')
right = 4 #input('How many meters do you want to go to the right:')

desX = int(forward/gridSize)
desY = int(right/gridSize)



def move(direction):
	if(direction == 0):
		Forward()
	elif(direction == -1):
		Left()
	elif(direction == 1):
		Right()
	else:
		pass

def detectObstacle(spot):
	distance = 3 #function
	if(distance < 1.5 * gridSize):
		obstacleList.append(spot)
		return True
	else:
		return False

def adjacentNSWE(direction):
	global myX
	global myY
	if(direction == 0):
		myX += 1
	elif(direction == 2):
		myX -= 1
	elif(direction == 1):
		myY += 1
	elif(direction == 3):
		myY -= 1

def turnRight():
	global myDir
	adjacentNSWE(myDir)
	myDir += 1
	if(myDir == 4):
		myDir = 0
	adjacentNSWE(myDir)

def turnLeft():
	print "fuck"
	global myDir
	adjacentNSWE(myDir)
	myDir -= 1
	if(myDir == -1):
		myDir = 3
	adjacentNSWE(myDir)


obstacleFound = True
while obstacleFound:
	print `myX` + " " + `myY`
	print myDir
	mySolution = getSolution(myX, myY, desX, desY, myDir, obstacleList)
	print mySolution[1]
	obstacleFound = False
	length = len(mySolution[1])

	for x in range(length):
		for movement in mySolution[1][x]:

			if(movement == 0 and detectObstacle(mySolution[0][x+1])):
				obstacleFound = True
				break;
			elif(movement == 1):
				turnRight()
				print "yes"
				obstacleFound = True
			elif(movement == -1):
				turnLeft()

				obstacleFound = True
				break;
			else:
				break;

		if(obstacleFound):
			break;
		else:
			myX = mySolution[0][x+1][0]
			myY = mySolution[0][x+1][1]
			myDir = getDirectionNSWE(mySolution[0][x], mySolution[0][x+1])

	if(myX == desX and myY == desY):
		break;


print "success!"