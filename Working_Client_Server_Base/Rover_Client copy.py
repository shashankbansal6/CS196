import socket 						# imports the socket api functionality.

class socketData:
	port 				= 1234
	hostname 			= 'localhost' 	# Local host for testing.
	readNumBytes		= 1024			# Read at most 1024 bytes of data
	connection			= None			# Bounded connection

'''
	Function:	Initializes the client socket
	Returns:	True 	-> Client Socket successefully created.
				False 	-> Client Socket unsuccessful in creation.
'''
def initialization(connection):
	if socketData.connection is None:
		socketData.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	# Obtains socket object.
		return True
	return False

'''
	Function:	Reads data when present from socket
	Returns:	None.
	Note:		Sleeps until reads "readNumBytes" or empty string
'''
def read(socketData):
	if socketData.connection is not None:
		try:
			socketData.connection.connect((socketData.hostname, socketData.port))		# Opens connection
			print socketData.connection.recv(socketData.readNumBytes)					# Prints bytes read
			return True
		except socket.error:
			print "Whoops, looks like you aren't connected."
			return False
	return False

'''
	Function:	Closes the client's connection
	Returns:	True 	-> Client was successefully disconnected.
				False 	-> Client was unsuccessful in disconnecting
						   (if never initialized).
'''
def halt(socketData):
	if socketData.connection is not None:
		socketData.connection.close()
		return True
	return False

def clientTest():
	data = socketData()
	if initialization(data) and read(data):
		halt(data)
		return True
	return False

if  __name__ =='__main__':
	if clientTest():
		print "Client Test was Successeful."
	else:
		print "Client Test was Unsuccessful."