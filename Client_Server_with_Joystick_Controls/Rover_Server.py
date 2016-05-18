import socket 						# imports the socket api functionality.
from threading import Thread 		# Needed to close server before requests run out.
import pygame
from pygame.locals import *

class socketData:
	port 				= 1234
	hostname 			= 'localhost' 	# Local host for testing.
	serverSocket 		= None			# The server where clients connect too.
	connectionRequests 	= 5				# Number of requests allowed (5 = default).
	running				= True			# Server running = True; Server stopped = false
	connectionCount		= 0				# Number of begining connections

'''
	Function:	Initializes the server.
	Returns:	True 	-> Server Socket successefully created.
				False 	-> Server Socket unsuccessful in creation.
'''
def initialization(socketData):
	if socketData.serverSocket is None:
		socketData.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)			# Obtains socket object.
		try:
			socketData.serverSocket.bind((socketData.hostname, socketData.port))				# Binds the host to the port number.
		except socket.error:
			print("Address is already in use. Reset to use.")
			return False
		socketData.serverSocket.listen(socketData.connectionRequests)						# Makes "connection" a server socket.
		return True
	return False

'''
	Function:	Listens for incoming connections and sends welcome message.
	Returns:	None.
'''
def connectionListen(socketData):
	print("Testing")
	while socketData.running and socketData.serverSocket is not None:
		(clientSocket, clientAddress) = socketData.serverSocket.accept()		# Wait and accept incoming connections.
		socketData.connectionCount += 1
		print(("Connection recieved from ", clientAddress))
		#clientSocket.send("HELLO WORLD.")										# Send Welcome message.
		#clientSocket.close()
		setupController();

'''
	Function:	Halts the server from further use (shutdown).
	Returns:	True 	-> Server Socket successefully shutdown.
				False 	-> Server Socket unsuccessful in halt
						   (if never initialized).
'''
def halt(socketData):
	if socketData.serverSocket is not None:
		socketData.serverSocket.close()											# Closes server from further usage.
		return True
	return False

def setupController():
	pygame.init()
	pygame.display.set_caption("JOYTEST")
	clock = pygame.time.Clock()
	joysticks = []
	for i in range(0, pygame.joystick.get_count()):
		joysticks.append(pygame.joystick.Joystick(i))
		joysticks[-1].init()
		print("Detected joystick '",joysticks[-1].get_name(),"'")
	while 1:
		clock.tick(60)
		for event in pygame.event.get():
			if(event.type == JOYBUTTONDOWN):
					print(("Joystick '",joysticks[event.joy].get_name(),"' button",event.button,"down."))
					if(event.button == 0):
						clientSocket.send("Up")
					elif(event.button == 1):
						clientSocket.send("Down")
					elif(event.button == 2):
						clientSocket.send("Left")
					elif(event.button == 4):
						clientSocket.send("Right")
			elif(event.type == JOYBUTTONUP):
					print("Joystick '",joysticks[event.joy].get_name(),"' button",event.button,"up.")
			elif(event.type == JOYHATMOTION):
					print("Joystick '",joysticks[event.joy].get_name(),"' hat",event.hat," moved.")

def serverTest():
	data = socketData()
	if initialization(data) is True:
		print("Server has been Initialized.")
	else:
		print("Server Failed to Initialize.")
		return False
	connectionListen(data)
	'''
	thread = Thread(target = connectionListen, args = (data,))
	thread.start()
	while data.connectionCount is 0 and data.serverSocket is not None:
		continue
	data.running = False
	thread.join()
	halt(data);
	'''
	print("Server halted.")
	return True

if  __name__ =='__main__':
	if serverTest() is True:
		print("Server Test was Successeful.")
	else:
		print("Server Test was Unsuccessful.")
