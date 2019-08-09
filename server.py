import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
a = socket.gethostname()
serverSocket.bind(("127.0.0.1", 8756))
serverSocket.listen(1)

while True:
    a = serverSocket.accept()

    bufferData = serverSocket.recv(32)
    if bufferData == b"begin":
        bufferData = serverSocket.recv(1024)
        while  bufferData:
            print("Got: ", bufferData.encode("utf-8"))
            bufferData = serverSocket.recv(1024)
            pass

    pass