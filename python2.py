#serialisacion combertir archivos a binario
import pickle

def serialisacion():
    nombre=input("nombre del archivo: ");
    contenido=input("contenido del archivo a serialisar: ");
    fichero=open(nombre,'wb');
    pickle.dump(contenido,fichero);
    fichero.close();
    del (fichero);
serialisacion();
