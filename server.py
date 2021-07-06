import socket

s = socket.socket()
host = "localhost"
port = 3000

s.bind((host,port))
s.listen(1)

print("waiting for connections :")
conn, addr=s.accept()
print(addr," has connected to the server ")

filename = input(str("enter the file name of the file :"))
file = open(filename, 'rb')
file_data = file.read(1024)
conn.send(file_data)
print("Data has been transmitted sucessfully")