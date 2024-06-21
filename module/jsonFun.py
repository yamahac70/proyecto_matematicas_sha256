import os
import tkinter as tk
import json
def load_json(ruta):
    if not os.path.exists(ruta):
        return {}  # Devuelve un diccionario vacío si el archivo no existe
    
    with open(ruta, 'r') as f:
        contenido = f.read()  # Lee todo el contenido del archivo como una cadena
        # Reemplaza las comillas simples por comillas dobles
        contenido_corregido={}
        if isinstance(contenido, str):
            contenido_corregido = contenido.replace("'", '"')
            contenido_corregido=contenido_corregido.strip('"')
        else:
            contenido_corregido=contenido
       # print(contenido_corregido)
        # Carga el JSON corregido como un objeto Python
        try:
            objeto_json = json.loads(contenido_corregido)
            return objeto_json
        except json.JSONDecodeError as e:
            print(f"Error al decodificar JSON en el archivo '{ruta}': {e}")
            tk.messagebox.showwarning("Error", f"Error al decodificar JSON en el archivo '{ruta}': {e}")
            return {}  # Devuelve un diccionario vacío en caso de error
def save_json(data, path):
    #print(data)
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)