import socket
    
port = 80

sock = socket.socket()
sock.bind(('', port))    

#print (('Starting server on', port))
#print ('The Web server URL for this would be http://%s:%d/' % (host, port))

sock.listen(1)
print("Listening ...")


while True:  
    client_host, client_port = sock.accept()
    data = client_host.recv(1024).decode()
    print(data)
   #client_host.sendall(bytearray('HTTP/1.0 200 OK\n',"ascii"))
    client_host.sendall(bytearray(data, "ascii"))
    client_host.close()
sock.close()
