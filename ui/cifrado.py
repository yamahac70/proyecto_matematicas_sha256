
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,filedialog,PhotoImage,messagebox
import os
import json
from module.encriptar import hashear_archivo
from datetime import date
from datetime import datetime
from module.correo import sendMailSimple
archivosHashD={"hashes":[]}
global canvas, ruta_texto,jsonText,btnEnviar,btnGuardar,textoGenera,inputCorreo
ruta_texto=None
def scale_image(img_path, width, height):
    # Cargar la imagen original en PhotoImage
    original_img = PhotoImage(file=img_path)

    # Escalar la imagen utilizando submuestreo (reduciendo la calidad)
    scaled_img = original_img.subsample(original_img.width() // width, original_img.height() // height)

    return scaled_img
def home(win):
    from ui.inicio import inicioUi
    win.destroy()
    inicioUi()
def cambio_ruta(ruta):
    global canvas, ruta_texto
    print(ruta)
    print(ruta_texto)
    canvas.itemconfig(ruta_texto, text=ruta)
def cambio_json(objetoJson):
    global jsonText
    
    json_str = json.dumps(objetoJson, indent=4, ensure_ascii=False)
    jsonText.config(state="normal")
    jsonText.delete("1.0", "end")  # Borra el contenido actual del Text
    jsonText.insert("1.0", json_str)  # Inserta el nuevo contenido JSON
    jsonText.config(state="disabled")
def carpetaInfo():
    global selected_path
    selected_path = filedialog.askdirectory()
    if selected_path == "":
        selected_path = None
    return selected_path
def obtener_rutas_archivos(carpeta):
    global rutas_archivos 
    
    rutas_archivos = []
    for root, _, files in os.walk(carpeta):
        for file in files:
            ruta_completa = os.path.join(root, file)
            ruta_completa = os.path.normpath(ruta_completa)
            rutas_archivos.append(ruta_completa)
    return rutas_archivos
def seleccionar_carpeta():
    ruta = carpetaInfo()
    if ruta:
        #label_ruta.config(text=f"Carpeta seleccionada: {ruta}")
        cambio_ruta(ruta)
        # Obtener las rutas de todos los archivos dentro de la carpeta seleccionada
        rutas_archivosRut = obtener_rutas_archivos(ruta)
        #print(rutas_archivosRut)
        #cambio_json({"hash":rutas_archivosRut})
        archivoHash(rutas_archivosRut)
        # Mostrar las rutas de los archivos (ejemplo)
        # mostrar_rutas_archivos(rutas_archivosRut)
    else:
        cambio_ruta("No se seleccionó ninguna carpeta")
def archivoHash(rutasArchivos):
    global btnEnviar,btnGuardar,textoGenera,canvas,inputCorreo
    archivosHashD["hashes"]=[]
    for i in rutasArchivos:
        now=datetime.now();
        fechaCompleta=f"{format(now.day)}/{format(now.month)}/{format(now.year)}, {format(now.hour)}:{format(now.minute)}:{format(now.second)}"
        print (i)
        arch=hashear_archivo(i)
        archivosHashD["hashes"].append({
        "archivo": i.split("\\")[len(i.split("\\"))-1],
        "hasher": arch,
        "fecha": fechaCompleta})
    cambio_json(archivosHashD)
    btnEnviar.place(
        x=524.0,
        y=318.0,
        width=107.0,
        height=35.0
    )
    btnGuardar.place(
        x=644.0,
        y=318.0,
        width=107.0,
        height=35.0
    )
    inputCorreo.place(
         x=324.0,
        y=318.0,
        width=207.0,
        height=35.0
    )
    canvas.itemconfig(textoGenera, text="Elija que hacer con el archivo generado")
def guardarArchivo():
    #buscamos el directorio donde guardaremos el archivo
    directorio = filedialog.asksaveasfilename(defaultextension=".json")
    if directorio:
        with open(directorio, "w") as archivo:
            json.dump(archivosHashD, archivo)
        messagebox.showinfo("Guardado", "El archivo ha sido guardado con exito")
def enviarArchivo():
    global inputCorreo
    inp = inputCorreo.get(1.0, "end-1c")
    if inp=="":
        inp="acostamaurojulian1@gmail.com"
    messagebox.showinfo("correo",f"se enviara a {inp}")
    sendMailSimple(inp,archivosHashD)
    messagebox.showinfo("correo",f"correo nviado")

def cifradoUi():
    global canvas, ruta_texto,jsonText,btnEnviar,btnGuardar,textoGenera,inputCorreo
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame1")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("785x386")
    window.configure(bg = "#4E93FC")


    canvas = Canvas(
        window,
        bg = "#4E93FC",
        height = 386,
        width = 765,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        164.0,
        190.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("Recurso_1.png"))
    
    image_2 = canvas.create_image(
        546.0,
        200.0,
        image=image_image_2
    )
    #correo texto
    inputCorreo=Text(window,
                     height = 5, 
                   width = 20)
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    btnEnviar = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: enviarArchivo(),
        relief="flat"
    )
   

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    btnGuardar = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: guardarArchivo(),
        relief="flat"
    )
    
    #x=444.0,
    #     y=318.0,
    textoGenera=canvas.create_text(
        560.0,318.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter SemiBold", 11 * -1)
    )
  
    texto=canvas.create_text(
        25.0,
        210.0,
        anchor="nw",
        text="Al seleccionar una carpeta, se mostrarán sus archivos",
        fill="#000000",
        font=("Inter SemiBold", 11 * -1)
    )
    

    btnCarpeta = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=btnCarpeta,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: seleccionar_carpeta(),
        relief="flat"
    )
    button_4.place(
        x=105.0,
        y=124.0,
        width=112.0,
        height=35.0
    )

    canvas.create_rectangle(
        25.0,
        162.0,
        304.0,
        205.0,
        fill="#D9D9D9",
        outline="")

    ruta_texto=canvas.create_text(
        25.0,
        176.0,
        anchor="nw",
        text="Ruta",
        fill="#000000",
        font=("Inter SemiBold", 12 * -1)
    )

    canvas.create_text(
        18.0,
        39.0,
        anchor="nw",
        text="CIFRADO SHA256",
        fill="#FFFFFF",
        font=("Inter Bold", 32 * -1)
    )
    canvas.create_text(
        18.0,
        73.0,
        anchor="nw",
        text="SE CREARA HASH DE TODOS LOS ARCHIVOS \n DE LA CARPETA SELECCIONADA",
        fill="#FFFFFF",
        font=("Inter Bold", 13 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        636.0,
        181.0,
        image=entry_image_1
    )
    jsonText = Text(
        bd=0,
        bg="#ffffff",
        fg="#000716",
        highlightthickness=1
        
    )
    #bg="#D9D9D9",
    jsonText.place(
        x=321.0,
        y=52.0,
        width=430.0,
        height=256.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: window.destroy(),
        relief="flat"
    )
    button_5.place(
        x=25.0,
        y=361.0,
        width=56.674713134765625,
        height=23.999988555908203
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: home(window),
        relief="flat"
    )
    button_6.place(
        x=84.0,
        y=361.0,
        width=56.674713134765625,
        height=23.999988555908203
    )
    window.resizable(False, False)
    window.mainloop()
