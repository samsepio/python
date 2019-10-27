import socket
from colorama import *

def wrshell():
    host=input(Fore.GREEN+"host: ");
    puerto=int(input("puerto: "));
    misocket=socket.socket();
    misocket.connect((host,puerto));
    mensaje="hola desde el esclavo";
    misocket.sendall(mensaje.encode('utf-8'));
    respuesta=misocket.recv(1024);
    print(respuesta)
wrshell();
