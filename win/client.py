import socket
import hashlib
import time

class Client:
    def __init__(self):
        try:
            self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.serverIp = "79.174.62.233"
            self.port = 5901
            self.buffSize = 1048576
            pass
        except Exception as identifier:
            print(identifier)
            pass
        self.textFileName = "test"

    def PullDict(self):
        self.clientSocket.connect((self.serverIp, self.port))
        self.clientSocket.send(b"pull")
        hash = self.clientSocket.recv(32).decode('utf-8')
        print("Got hash: ", hash)
        self.textFileName = "C:\Personal\ElinorTranslater\\tato-wordlist.xlsx"
        with open(self.textFileName, "w+b") as file:
            bufferData = self.clientSocket.recv(self.buffSize)
            while bufferData != b"":
                print(bufferData)
                file.write(bufferData)
                bufferData = self.clientSocket.recv(self.buffSize)
            file.close()
            md5Summ = hashlib.md5(open(self.textFileName, "rb").read()).hexdigest()
            print(hash,"\n", md5Summ)
            if hash == md5Summ:
                print("transmission ended. got file {0}", self.textFileName)
            else:
                print('bad hash')
        self.clientSocket.close()
    
    def PushDict(self):
        self.clientSocket.connect((self.serverIp, self.port))
        self.clientSocket.send(b'push')
        time.sleep(1)
        self.textFileName = "C:\Personal\ElinorTranslater\\tato-wordlist.xlsx"
        hash  = hashlib.md5(open(self.textFileName, 'rb').read()).hexdigest()
        self.clientSocket.send(hash.encode('utf-8'))
        serverConfirm = b''
        while serverConfirm != b'succ':
            with open(self.textFileName, "rb") as file:
                bufferData = file.read(self.buffSize)
                a = file.read(self.buffSize)
                while bufferData:
                    self.clientSocket.send(bufferData)
                    bufferData = file.read(self.buffSize)
                file.close()
                time.sleep(1)
                self.clientSocket.send(b'endl')
                serverConfirm = self.clientSocket.recv(4)
                while not serverConfirm:
                    self.clientSocket.send(b'endl')
                    serverConfirm = self.clientSocket.recv(4)
                    time.sleep(1)
                
                print(serverConfirm)
        self.clientSocket.close()
        print("transmission ended. got file {0}", self.textFileName)

