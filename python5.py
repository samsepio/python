import socket

def misocket():
    host=input("host: ");
    puerto=input("puerto: ");
    mi_socket = socket.socket()
    mi_socket.connect((str(host),int(puerto)));
    mi_socket.listen(5);
    while True:
        conexion, addr= mi_socket.accept()
        print("nueva conexion establecida!!!");
        print(addr);
        peticion=conexion.recv(1024);
        print(peticion);
        mensaje=input("mensaje: ");
        conexion.send(mensaje.encode());
        conexion.close();
misocket();
