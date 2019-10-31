import urllib,urllib.request
import subprocess
import shutil
from colorama import *

def downloadcode():
    subprocess.run(['clear']);
    url=input(Fore.GREEN+"url del sitio a descargar: ");
    nombre=input("nombre del archivo a descargar: ");
    destino=input("directorio del archivo a descargar: ");
    print(Fore.YELLOW+"descargando arhivo.../");
    html_handler = urllib.request.urlopen(url);
    html=str(html_handler.read(),'utf-8');
    file_handler=open(nombre,'w');
    file_handler.write(html);
    shutil.move(nombre,destino);
    print(Fore.BLUE+"archivo descargado exitosamente!!!");
downloadcode();


