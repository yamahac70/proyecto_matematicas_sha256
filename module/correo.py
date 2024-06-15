#https://docs.python.org/es/3/library/smtplib.html
#https://gist.github.com/2624789/d42aaa12bf3a36356342
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
import json
#from email.mime.multipart import MIMEMultipart
#from email.mime.text import MIMEText
#from email.mime.base import MIMEBase
#from email import encoders
#import os
contrasenia="ealq jwva fiac ivwa"
email="notasfinallab1@gmail.com"
def send_email(destino="acostamaurojulian1@gmail.com",body="hola"):
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = destino  # Reemplaza con la dirección del destinatario
    msg['Subject'] = 'Asunto del correo'
    try:
        # Abrimos el archivo que vamos a adjuntar
        archivo_adjunto = open('encriptados.zip', 'rb')
        adjunto_MIME = MIMEBase('application', 'octet-stream')
        # Y le cargamos el archivo adjunto
        adjunto_MIME.set_payload((archivo_adjunto).read())
        # Codificamos el objeto en BASE64
        encoders.encode_base64(adjunto_MIME)
        adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
        msg.attach(adjunto_MIME)
        ###################333
        server = SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, contrasenia)
        msg.attach(MIMEText(body, 'plain'))
        server.sendmail(email, destino, msg.as_string())
        server.quit()
    except:
        print("Error al enviar el correo")
    finally:
        server.quit()
        
def sendMailSimplec(destino="acostamaurojulian1@gmail.com",msg=""):
    server = SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, contrasenia)
    #msg.attach(MIMEText(body, 'plain'))
    #######################
     # Crear el mensaje
    message = MIMEMultipart()
    message['From'] = email
    message['To'] = destino
    message['Subject'] = 'JSON Data'
    
     # Adjuntar el cuerpo del mensaje
    message.attach(MIMEText(msg, 'plain'))
    ########################
    server.sendmail(email, destino, message.as_string())
    server.quit()
        
        
    #server = SMTP('smtp.gmail.com', 587)
    #server.starttls()
    #server.login(email, contrasenia)
    #msg.attach(MIMEText(body, 'plain'))
    #server.sendmail(email, "acostamaurojulian1@gmail.com", "hola")

def sendMailSimple(destino="acostamaurojulian1@gmail.com",msg=""):
    server = SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, contrasenia)
    
    # Crear el mensaje
    message = MIMEMultipart()
    message['From'] = email
    message['To'] = destino
    message['Subject'] = 'JSON Data'
    
    # Adjuntar el cuerpo del mensaje
    message.attach(MIMEText("Por favor, encuentra el archivo JSON adjunto.", 'plain'))
    
    # Convertir el mensaje a JSON y guardarlo en un archivo temporal
    #json_data = json.dumps(msg)
    filename = "data.json"
   # with open(filename, 'w') as json_file:
   #     json_file.write(json.dumps(msg, indent=4,ensure_ascii=False))
    with open(filename, "w") as archivo:
            json.dump(msg, archivo)
    #d=open(filename,"w")
    #d.write(msg)
    # Adjuntar el archivo JSON
    attachment = open(filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename={filename}')
    message.attach(part)
    attachment.close()
    
    # Enviar el correo
    server.sendmail(email, destino, message.as_string())
    server.quit()
