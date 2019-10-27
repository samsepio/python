import smtplib
import subprocess
import getpass
from colorama import *

def sendmail():
    subprocess.run(['clear']);
    try:
        correo=input(Fore.GREEN+"correo Electronico: ");
        contraseña=getpass.getpass("contraseña: ");
        destinatario=input("destinatario: ");
        mensaje=input("mensaje: ");
        print(Fore.YELLOW+"enviando mensaje.../");
        server=smtplib.SMTP('smtp.gmail.com','587');
        server.starttls();
        server.login(correo,contraseña);
        server.sendmail(correo,destinatario,mensaje);
        print(Fore.BLUE+"mensaje enviado exitosamente!!")
        server.quit();
    except KeyboardInterrupt:
        print(Fore.RED+"\n finalisado!!!");
    except smtplib.SMTPAuthenticationError:
        print(Fore.RED+"\n fallo de autenticacion");
sendmail();
