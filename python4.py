import os
from io import open

def programa():
    print('~~~~~~~ADMINISTRADOR DE ARCHIVOS~~~~~~~~');
    opcion=input('indique su opcion  \n  c=crear e=eliminar: ');
    if(opcion == "c" or opcion == "C"):
        opcionB=input("introdusca su opcion \n A=archivo C=carpeta: ");
        if(opcionB == "C" or opcionB == "c"):
            carpeta=input("nombre de la carpeta a crear: ");
            os.mkdir(carpeta);
            print('carpeta',carpeta,'creada con exito');
        if(opcionB == "A" or opcionB == "a"):
            nombre=input("nombre del archivo a crear: ");
            contenido=input("contenido del archivo a crear: ");
            archivo=open(nombre,'w');
            archivo.write(contenido);
            archivo.close();
            print('archivo',nombre,'creado exitosamente');
programa(); 
