import socket
serverName = '192.168.43.1'

serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = input('Input lowercase sentence:')
clientSocket.sendto(bytes(message,'utf-8'),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage)
clientSocket.close()
