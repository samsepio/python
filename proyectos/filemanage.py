from colorama import *
import os
import shutil
from io import open

def filemanage():
    try:
        opcion=input(Fore.GREEN+"Indique Su Opcion \n C=crear \n E=eliminar \n : ");
        if(opcion=="c" or opcion=="C"):
            opcionB=input(Fore.YELLOW+"Indique Su Opcion \n A=archivo \n C=carpeta \n : ");
            if(opcionB=="a" or opcionB=="A"):
                while True:
                    nombre=input(Fore.BLUE+"nombre del archivo a crear: ");
                    contenido=input(Fore.BLUE+"contenido del archivo: ");
                    break;
                archivo=open(nombre,'w');
                archivo.write(contenido);
                archivo.close();
            if(opcionB=="c" or opcionB=="C"):
                nombreB=input("nombre de la carpeta a crear: ");
                os.mkdir(nombreB);
        if(opcion=="e" or opcion=="E"):
            opcionC=input(Fore.YELLOW+"Indique Su Opcion \n A=archivo \n C=carpeta \n :  ");
            if(opcionC=="a" or opcionC=="A"):
                nombreC=input(Fore.BLUE+"nombre del archivo a eliminar: ");
                os.remove(nombreC);
            if(opcionC=="c" or opcionC=="C"):
                nombreD=input("nombre de la carpeta a eliminar: ");
                shutil.rmtree(nombreD);
    except KeyboardInterrupt:
        print(Fore.RED+"\n finalisado...");
    except FileNotFoundError:
        print(Fore.RED+"\n el archivo o carpeta dicho no existe");
filemanage();
