import socket as soc
import os 
import threading
import pyfiglet


## your ip 
SenderIP = input("Enter Sender IP Address: ")
ReceiverIP = input("Enter Receiver Ip Address:")
Port = int(input("Enter  port: "))


## Creating UDP Socket
ReadySocket = soc.socket(soc.AF_INET,soc.SOCK_DGRAM)

## only for Reciving messages 
ReadySocket.bind((SenderIP,Port))


os.system('clear')  ## For linux use os.system('clear')
print(pyfiglet.figlet_format('CHAT_WEB _APP'))


## Sending message function
def SendMsg():
        while True:
                Message = input()
                print("\n")
                if(Message == 'quite' or Message == 'bye' or Message == 'exit'):    
                       Message = 'Your Friend is offline'    
                       ReadySocket.sendto(Message.encode(),(ReceiverIP,Port))
                       os._exit(1)
                else:
                     ReadySocket.sendto(Message.encode(),(ReceiverIP,Port))
                    

## Receving message function
def RecvMsg():
        while True:
                Msg = ReadySocket.recvfrom(100)
                print("\n\t\t\t\t" + Msg[1][0] + ":" + Msg[0].decode())
               

## Created 2 Threads for sending and reciving msg parllerl
SendMsg = threading.Thread(target=SendMsg)
RecvMsg = threading.Thread(target=RecvMsg)


## starting thread 
SendMsg.start()
RecvMsg.start()




