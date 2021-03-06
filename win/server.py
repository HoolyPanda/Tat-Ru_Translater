import socket
import hashlib
import os

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
a = socket.gethostname()
serverSocket.bind(("192.168.0.103", 5901))
serverSocket.listen(1)

while True:
    conn, addr = serverSocket.accept()

    bufferData = conn.recv(4)
    buffSize = 1048576
    if bufferData == b"pull":
        textFileName = "tato-wordlist.xlsx"
        md5Summ = hashlib.md5(open(textFileName, "rb").read()).hexdigest()
        print(hashlib.md5(open(textFileName, "rb").read()))
        conn.send(md5Summ.encode('utf-8'))
        with open(textFileName, "rb") as file:
            bufferData = file.read(buffSize)
            while bufferData:
                print("Data to send", bufferData)
                try:
                    conn.send(bufferData)
                    pass
                except Exception as identifier:
                    print("sending Error: ", identifier)
                    pass
                bufferData = file.read(buffSize)
            file.close()
            conn.close()
            print("transmission ended")
            
    elif bufferData == b"push":
        print("got push rec")
        textFileName = "tato-wordlist1.xlsx"
        hash = conn.recv(32).decode('utf-8')
        with open(textFileName, "w+b") as file:
            bufferData = conn.recv(buffSize)
            print(bufferData)
            while bufferData != b"endl":
                file.write(bufferData)
                bufferData = conn.recv(buffSize)
                print(bufferData)
            file.close()
            localHash = hashlib.md5(open(textFileName,'rb').read()).hexdigest()
            print(hash, '\n', localHash)
            if hash == localHash:
                print("transmission ended. got file {0}", textFileName)
                conn.send(b'succ')
                os.remove('./tato-wordlist.xlsx')
                os.rename('./tato-wordlist1.xlsx', './tato-wordlist.xlsx')
            else:
                print('Bad Hash')
    else:
        print(bufferData)


    pass
