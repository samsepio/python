import socket

def sockets():
    host=input("host: ");
    puerto=input("puerto: ");
    mi_socket = socket.socket();
    mi_socket.connect(str(host),int(puerto));
    mensaje=input("mensaje: ");
    mi_socket.send(mensaje.encode());
    respuesta = mi_socket.recv(1024);
    print(respuesta)
    mi_socket.close();
sockets();
