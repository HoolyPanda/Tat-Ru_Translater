import socket
import hashlib
import time

class Client:
    def __init__(self):
        try:
            self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.port = 5901
            pass
        except Exception as identifier:
            print(identifier)
            pass
        self.textFileName = "test"

    def PullDict(self):
        self.clientSocket.connect(("79.174.62.233", self.port))
        self.clientSocket.send(b"pull")
        hash = self.clientSocket.recv(32).decode('utf-8')
        print("Got hash: ", hash)
        self.textFileName = "tato-wordlist.xlsx"
        with open(self.textFileName, "w+b") as file:
            bufferData = self.clientSocket.recv(1024)
            while bufferData is not b"":
                print(bufferData)
                file.write(bufferData)
                bufferData = self.clientSocket.recv(1024)
            file.close()
            md5Summ = hashlib.md5(open(self.textFileName, "rb").read()).hexdigest()
            print(hash,"\n", md5Summ)
            if hash == md5Summ:
                print("transmission ended. got file {0}", self.textFileName)
            else:
                print('bad hash')
        self.clientSocket.close()
    
    def PushDict(self):
        self.clientSocket.connect(("127.0.0.1", self.port))
        self.clientSocket.send(b'push')
        time.sleep(1)
        self.textFileName = "tato-wordlist.xlsx"
        hash  = hashlib.md5(open(self.textFileName, 'rb').read()).hexdigest()
        self.clientSocket.send(hash.encode('utf-8'))
        with open(self.textFileName, "rb") as file:
            # bufferData = self.clientSocket.recv(1024)
            bufferData = file.read(1024)
            while bufferData:
                self.clientSocket.send(bufferData)
                bufferData = file.read(1024)
            file.close()
        print("transmission ended. got file {0}", self.textFileName)

# client = Client()
# client.PullDict()
# client.PushDict()