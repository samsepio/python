import socket
from colorama import *

def wrshell():
    host=input(Fore.GREEN+"host: ");
    puerto=int(input(Fore.GREEN+"puerto: "));
    misocket=socket.socket();
    misocket.bind((host,puerto));
    misocket.listen(4);
    while True:
        conexion, addr=misocket.accept();
        print("nueva conexion establecida");
        print(addr);
        mensaje="hola esclavo te hackeare";
        misocket.sendall(mensaje.encode('utf-8'));
wrshell();

