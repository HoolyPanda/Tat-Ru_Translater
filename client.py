import socket

try:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(("127.0.0.1", 8756))
    pass
except Exception as identifier:
    print(identifier)
    pass

textFileName = "test"
clientSocket.send(b"begin")
with open(textFileName, "rb") as file:
    bufferData = file.read(1024)
    while bufferData:
        print("Data to send", bufferData.decode("utf-8"))
        try:
            clientSocket.send(bufferData)
            pass
        except Exception as identifier:
            print("sending Error: ", identifier)
            pass
        bufferData = file.read(1024)
    file.close()
bufferData = clientSocket.recv(1024)
while bufferData:
    print(bufferData.encode("utf-8"))
    pass

