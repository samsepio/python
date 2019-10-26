import glob,os.path

#glob nos permite indexar en la ruta seleccionada para indexar los archivos y documentos que contiene

#path es un submodulo de os, que nos permitira entre otras cosas saber si un archivo o carpeta existe en la ruta indicada

def directorio():
    directorio=input("ingrese la carpeta: ");
    todo=glob.glob(directorio + '/*');
    print('todo lo que hay es este directorio',todo);
    archivos = []
    for element in todo:
        if(os.path.isfile(element)):
            archivos.append(element)
    print("todos los archivos del directorio: ",archivos);
    carpetas = []
    for element in todo:
        if(os.path.isdir(element)):
            carpetas.append(element);
    print("todas las carpetas del directorio: ",carpetas);    
    #archivos con estencion .txt
    txt = glob.glob("../python/*.txt");
    py = glob.glob("../python/*.py");
    print('archivos con extencion txt',txt);
    print('archivos con extencion python',py);
    #archivo de caracteres x representado por ?
    txt3char = glob.glob('../python/????.txt');
    print('todos los archivos de cuatro caracteres extencion txt: ',txt3char);
directorio();
