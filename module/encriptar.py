import hashlib
import os
#https://helix.stormhub.org/papers/SHA-256.pdf
def hashear_archivo(ruta_archivo, algoritmo='sha256'):
    # Crear un objeto de hash del algoritmo especificado
    hash_obj = hashlib.new(algoritmo)
    
    # Leer el archivo en modo binario y actualizar el objeto de hash
    with open(ruta_archivo, 'rb') as archivo:
        while True:
            # Leer el archivo en bloques de 4096 bytes
            bloque = archivo.read(4096)
            if not bloque:
                break
            hash_obj.update(bloque)
    
    # Obtener el hash final en formato hexadecimal
    hash_hex = hash_obj.hexdigest()
    
    # Obtener la carpeta donde se encuentra el archivo original
    carpeta_origen = os.path.dirname(ruta_archivo)
    
    # Obtener el nombre del archivo sin la ruta completa
    #nombre_archivo = os.path.basename(ruta_archivo)
    
    # Construir la ruta para el archivo de hash en la misma carpeta
    #ruta_hash = os.path.join(carpeta_origen, f"{nombre_archivo}.{algoritmo}")
    # Guardar el hash en un archivo en la misma carpeta
    # Verificar si la carpeta "./encriptados/" existe y crearla si no existe
    #if not os.path.exists("./encriptados"):
    #    os.makedirs("./encriptados")
    #    
    #ruta_programa=f"./encriptados/{nombre_archivo}.{algoritmo}"
    #
    #
    #with open(ruta_hash, 'w') as archivo_hash:
    #    archivo_hash.write(hash_hex)
    #with open(ruta_programa, 'w') as archivo_programa:
    #    archivo_programa.write(hash_hex)
   
    return hash_hex

def verificar_hash(ruta_archivo, hash_guardado, algoritmo='sha256'):
    # Crear un objeto de hash del algoritmo especificado
    hash_obj = hashlib.new(algoritmo)
    
    # Leer el archivo en modo binario y actualizar el objeto de hash
    with open(ruta_archivo, 'rb') as archivo:
        while True:
            # Leer el archivo en bloques de 4096 bytes
            bloque = archivo.read(4096)
            if not bloque:
                break
            hash_obj.update(bloque)
    
    # Obtener el hash final en formato hexadecimal
    hash_calculado = hash_obj.hexdigest()
    
    # Comparar el hash calculado con el hash guardado
    if hash_calculado == hash_guardado:
        return True
    else:
        return False
#hashear_archivo('E:/iso/G-U-7LTE32B/32/GU7LTE32B.iso')
#print(os.path.dirname(os.path.realpath(__file__)))