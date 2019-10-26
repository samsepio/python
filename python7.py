from colorama import *
import smtplib
import getpass

def sendemail():
    mensaje=input(Fore.GREEN + "introdusca su mensaje: ");
    correo=input(Fore.GREEN + "introdusca su correo: ");
    destino=input(Fore.GREEN + "introdusca el destinatario: ")
    contraseña=getpass.getpass(Fore.GREEN+'introdusca su contraseña: ');
    
    server = smtplib.SMTP('smtp.gmail.com',587);
    server.starttls();
    server.login(correo,contraseña);
    try:
        server.sendmail(correo,destino,mensaje);
        server.quit();
        print(Fore.BLUE + "correo enviado exitosamente");
    except smtplib.SMTPAuthenticationError: 
        print(Fore.RED + 'A ocurrido un error');
sendemail();

