from socket import *
import tkinter as tk
import threading



listOfTrustedPeers = [] # ona be man trust daran
listOfTrustingPeers = [] # man be ona trust daram
ListOfNews = [] # khabar haye man ke enteshar dadam
listenednews = [] #khabar hayi ke ta be hal shenide shode and

s=socket(AF_INET, SOCK_STREAM)
s.connect(("8.8.8.8",80))
myIp=s.getsockname()[0]
s.close()
print(myIp)

def trustrequest(ip):
    #ip o port girande ke bayad dar list of trusting peers ezafe shavad
    serverName =ip
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    message = "trustreques%none%none"
    clientSocket.send(message.encode())
    modifiedMessage = clientSocket.recv(1024)
    if(modifiedMessage.decode() == "trustrequestaccepted"):
        listOfTrustingPeers.append(serverName)
        print(listOfTrustingPeers)
    clientSocket.close()

def trustaccept(ip):
    # ip o port ferestande bayad be list of trusted peers ezafe shavad
    listOfTrustedPeers.append(ip)

def shareNews(requested):
    #news be list news ezafe mishavad
    #bayad be hameye list trusted ha ersal konad
    for i in listOfTrustedPeers:
        serverName =i
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName,12000))
        message = requested+"%"+myIp
        clientSocket.send(message.encode())
        modifiedMessage = clientSocket.recv(1024)
        clientSocket.close()

def recieveNews(request):
    news=request.split("%")
    print(news[3]+ "\ntitle: "+news[1] + "\ntext:\n"+news[2]+"\n\n")
    shareNews(request)


def handlesearch(forsearch,connectionSocket):
    for i in listOfTrustingPeers:
        serverName =i
        print(i)
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName,12000))
        message = "searchrequest%"+forsearch+"%none%"+myIp
        clientSocket.send(message.encode())
        modifiedMessage = clientSocket.recv(1024).decode()
        print(modifiedMessage)
        while (modifiedMessage!="none"):
            connectionSocket.send(modifiedMessage.encode())
            modifiedMessage = clientSocket.recv(1024).decode()
            print(modifiedMessage)
        clientSocket.close()
    connectionSocket.send("none".encode())


def searchrequest(forsearch):
    print("req send")
    for i in listOfTrustingPeers:
        serverName =i
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName,12000))
        message = "searchrequest%"+forsearch+"%none%"+myIp
        clientSocket.send(message.encode())
        modifiedMessage = clientSocket.recv(1024).decode()
        while (modifiedMessage!="none"):
            string=modifiedMessage.split("%")
            print(string[3]+ "\ntitle: "+string[1] + "\ntext:\n"+string[2]+"\n\n")
            modifiedMessage = clientSocket.recv(1024).decode()
        clientSocket.close()

















def ui():
    root= tk.Tk()

    canvas1 = tk.Canvas(root, width = 300, height = 280,  relief = 'raised')
    canvas1.pack()
    ###
    label1 = tk.Label(root, text='Enter the IP here:')
    label1.config(font=('helvetica', 10))
    canvas1.create_window(90, 10, window=label1)


    entry1 = tk.Entry (root)
    canvas1.create_window(100, 30, window=entry1)
    ###
    label2 = tk.Label(root, text='Enter the key to search:')
    label2.config(font=('helvetica', 10))
    canvas1.create_window(80, 220, window=label2)

    entry2 = tk.Entry (root)
    canvas1.create_window(100, 240, window=entry2)
    ###

    label3 = tk.Label(root, text='Enter your news here:')
    label3.config(font=('helvetica', 10))
    canvas1.create_window(70, 70, window=label3)

    label4 = tk.Label(root, text='Enter the title:')
    label4.config(font=('helvetica', 10))
    canvas1.create_window(80, 90, window=label4)

    label5 = tk.Label(root, text='Enter the text:')
    label5.config(font=('helvetica', 10))
    canvas1.create_window(80, 130, window=label5)


    entry3 = tk.Entry (root)
    padx = 10
    pady = 10
    entry3.pack(padx=padx, pady=pady)
    canvas1.create_window(100, 110, window=entry3)

    entry4 = tk.Entry (root)
    canvas1.create_window(100, 150, window=entry4)

    def getIpAddressToTrust():
        x1 = entry1.get()
        trustrequest(x1)
    def getWantedNews():
        x2 = entry2.get()
        searchrequest(x2)
    def spreadNews():
        x3 = entry3.get()
        x4 = entry4.get()
        strToSpread=x3+"%"+x4
        print(strToSpread)
        ListOfNews.append((x3 ,x4))
        shareNews("newsrequest%"+strToSpread)

    button1 = tk.Button(text='Trust', command=getIpAddressToTrust, bg='black', fg='red', font=('helvetica', 9, 'bold'))
    canvas1.create_window(250, 20, window=button1)

    button2 = tk.Button(text='Search', command=getWantedNews, bg='black', fg='red', font=('helvetica', 9, 'bold'))
    canvas1.create_window(250, 230, window=button2)

    button3 = tk.Button(text='Spread', command=spreadNews, bg='black', fg='red', font=('helvetica', 9, 'bold'))
    canvas1.create_window(250, 150, window=button3)

    root.mainloop()




threading.Thread(target=ui).start()



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
    elif(request[0] ==  "newsrequest"):
        if(myIp not in request):#agar khabar ra qablan nadidam
            recieveNews(sentence)
            connectionSocket.send("newsrecieved".encode())
            connectionSocket.close()
        else:
            connectionSocket.send("newsrecieved".encode())
            connectionSocket.close()
    elif(request[0] == "searchrequest"):
        print(request)
        if(myIp in request):
            print("i searched it before")
            connectionSocket.send("none".encode())
            connectionSocket.close()
        else:
            print("i didnt search it before")
            for i in ListOfNews :
                if(request[1] in i[0]):
                    print("i have the news")
                    str1="searchresponse%"+i[0]+"%"+i[1]+"%"+myIp
                    connectionSocket.send(str1.encode())
            handlesearch(request[1],connectionSocket)
            connectionSocket.close()
