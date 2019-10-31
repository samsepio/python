import smtplib
import subprocess
import getpass
from colorama import *

def sendmail():
    subprocess.run(['clear']);
    try:
        correo=input(Fore.GREEN+"correo Electronico: ");
        contraseña=getpass.getpass("introdusca su contraseña: ");
        destinatario=input("destinatario del mensaje: ");
        mensaje=input("mensaje: ");
        print(Fore.YELLOW+"enviando correo../");
        server = smtplib.SMTP('smtp.gmail.com','587');
        server.starttls();
        server.login(correo,contraseña);
        server.sendmail(correo,destinatario,mensaje);
        server.quit();
        print(Fore.BLUE+"correo enviado exitosamente!!!");
    except KeyboardInterrupt:
        print(Fore.RED+"\n finalisado!!!");
    except smtplib.SMTPAuthenticationError:
        print(Fore.RED+"\n fallo de autenticacion");
sendmail();
