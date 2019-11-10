import socket
import time
 
HOST = '192.168.4.8'
PORT = 8008
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock.bind((HOST, PORT))  
sock.listen(5)
print('ip=%s:%s'%(HOST,PORT)) 
print('sever is listenning ......') 
while True:  
    connection,address = sock.accept()  
    try:  
        #connection.settimeout(10)  
        buf = connection.recv(1024)  
        if buf:  
            connection.send(b'welcome to server!')
            print(buf)
        else:  
            connection.send(b'please go out!')  
    except socket.timeout:  
        print ('time out')
    connection.close()  
 