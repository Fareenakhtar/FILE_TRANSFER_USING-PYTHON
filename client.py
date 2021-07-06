import socket 

s = socket.socket()

host = input(str("please enter the host address of the sender :"))
port = 3000
s.connect((host,port))
print("connected")

filename = input(str("enter a file name :"))
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
print("file received") 