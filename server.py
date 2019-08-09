import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
a = socket.gethostname()
serverSocket.bind(("192.168.0.102", 8757))
serverSocket.listen(1)

while True:
    conn, addr = serverSocket.accept()

    bufferData = conn.recv(32)
    if bufferData == b"begin":
        bufferData = conn.recv(1024)
        while  bufferData:
            print("Got: ", bufferData.decode("utf-8"))
            bufferData = conn.recv(1024)
            pass

    pass
