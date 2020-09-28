from socket import *
listOfTrustedPeers = [] # ona be man trust daran
listOfTrustingPeers = [] # man be ona trust daram
ListOfNews = [] # khabar haye man ke enteshar dadam




def trustrequest(ip,port):
    print("heh")
    #ip o port girande ke bayad dar list of trusting peers ezafe shavad
    serverName =ip
    serverPort = port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    print("connect nashode")
    clientSocket.connect((serverName,serverPort))
    print("connect shode")
    message = "trustreques%none%none"
    clientSocket.send(message.encode())
    modifiedMessage = clientSocket.recv(1024)
    if(modifiedMessage.decode() == "trustrequestaccepted"):
        print("hello")
        listOfTrustingPeers.append((serverName,serverPort))
        print(listOfTrustingPeers)
    clientSocket.close()

def trustaccept(ip):
    # ip o port ferestande bayad be list of trusted peers ezafe shavad
    listOfTrustedPeers.append(ip)


def shareNews(newstitle,newstext,ipOfWriter):
    #news be list news ezafe mishavad
    #bayad be hameye list trusted ha ersal konad
    for i in listOfTrustedPeers:
        serverName =i
        print(serverName)
        serverPort =12000
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName,serverPort))
        message = "news%"+newstitle+"%"+newstext+"%"+ipOfWriter
        clientSocket.send(message.encode())
        modifiedMessage = clientSocket.recv(1024)
        clientSocket.close()

def recieveNews(ip,port,title,text,ipOfWriter):
    print(ip+" / "+ str(port) + "\ntitle: "+title + "\ntext:\n"+text+"\n\n")
    if(ipOfWriter!="192.168.43.9")
        shareNews(title,text,ipOfWriter)
"""

def search(forseach):
    #bayad be hameye list trusting ha ersal shavad

"""

print("sag")
#trustrequest("192.168.43.102",12000)
print("khar")

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)
print ("The server is ready to receive")
while 1:
    connectionSocket, addr = serverSocket.accept()
    print("accept kard")
    sentence = connectionSocket.recv(1024).decode()
    request=sentence.split("%")
    if(request[0] == "trustreques"):
        trustaccept(addr[0])
        connectionSocket.send("trustrequestaccepted".encode())
        connectionSocket.close()
        print("sag")
        print(listOfTrustedPeers)
    elif(request[0] ==  "news"):
        recieveNews(addr[0],addr[1],request[1],request[2],request[3])
        connectionSocket.send("newsrecieved".encode())
        connectionSocket.close()
