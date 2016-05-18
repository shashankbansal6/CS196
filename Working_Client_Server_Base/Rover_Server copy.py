import socket 						# imports the socket api functionality.
from threading import Thread 		# Needed to close server before requests run out.

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
			print "Address is already in use. Reset to use."
			return False
		socketData.serverSocket.listen(socketData.connectionRequests)						# Makes "connection" a server socket.
		return True
	return False

'''
	Function:	Listens for incoming connections and sends welcome message.
	Returns:	None.
'''
def connectionListen(socketData):
	while socketData.running and socketData.serverSocket is not None:
		(clientSocket, clientAddress) = socketData.serverSocket.accept()		# Wait and accept incoming connections.
		socketData.connectionCount += 1
		print "Connection recieved from ", clientAddress
		clientSocket.send("HELLO WORLD.")										# Send Welcome message.
		clientSocket.close()

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

def serverTest():
	data = socketData()
	if initialization(data) is True:
		print "Server has been Initialized."
	else:
		print "Server Failed to Initialize."
		return False
	thread = Thread(target = connectionListen, args = (data,))
	thread.start()
	while data.connectionCount is 0 and data.serverSocket is not None:
		continue
	data.running = False
	thread.join()
	halt(data);
	print "Server halted."
	return True

if  __name__ =='__main__':
	if serverTest() is True:
		print "Server Test was Successeful."
	else:
		print "Server Test was Unsuccessful."
