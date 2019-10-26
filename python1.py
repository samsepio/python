from io import open 

print('----CREADOR DE ARCHIVOS---');
def filecreate():
    opcion=str(input("introdusca su opcion: "));
    if(opcion == 'w' or opcion== 'W'  ):
        nombre=input("introdusca el nombre del archivo: ");
        contenido=input("introdusca el contenido del archivo: ");
        archivo=open(nombre,'w');
        archivo.write(contenido);
        archivo.close();
    if(opcion == 'r' or opcion== 'R'):
        nombre=input("introdusca el nombre del archivo a leer: ");
        archivoR=open(nombre,'r');
        texto=archivoR.read();
        archivoR.close();
        print('conteido del archivo: ',texto);
    if(opcion == 'a' or opcion=='A'):
        nombre=input("nombre del archivo: ");
        agregar=input("text a a gregar en el archivo: ");
        archivoA=open(nombre,'a');
        archivoA.write(agregar);
        archivoA.close();
filecreate();
