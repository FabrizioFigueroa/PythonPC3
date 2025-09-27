import zipfile
import os
import requests

def descargar_imagen_url():
    url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    
    nombre_archivo = input("Ingrese nombre para la imagen (sin extension): ").strip()
    if not nombre_archivo:
        nombre_archivo = "imagen_descargada"
    
    nombre_archivo += ".jpg"
    
    try:
        print("Descargando imagen...")
        response = requests.get(url)
        response.raise_for_status()
        
        with open(nombre_archivo, 'wb') as file:
            file.write(response.content)
        
        print(f"Imagen descargada exitosamente: {nombre_archivo}")
        print(f"Tamano: {os.path.getsize(nombre_archivo)} bytes")
        return nombre_archivo
        
    except Exception as e:
        print(f"Error al descargar imagen: {e}")
        return None

def comprimir_imagen():
    print("1. Usar imagen de URL predefinida")
    print("2. Usar imagen local")
    opcion = input("Seleccione opcion: ").strip()
    
    if opcion == "1":
        ruta_imagen = descargar_imagen_url()
        if not ruta_imagen:
            return
    else:
        ruta_imagen = input("Ingrese la ruta completa de la imagen: ").strip()
        if not os.path.exists(ruta_imagen):
            print("La imagen no existe en la ruta especificada")
            return
    
    nombre_zip = input("Ingrese el nombre del archivo ZIP (sin extension): ").strip()
    if not nombre_zip:
        nombre_zip = "imagen_comprimida"
    
    nombre_zip += ".zip"
    
    try:
        with zipfile.ZipFile(nombre_zip, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            zip_file.write(ruta_imagen, os.path.basename(ruta_imagen))
        
        print(f"Imagen comprimida exitosamente en: {nombre_zip}")
        print(f"Tamano original: {os.path.getsize(ruta_imagen)} bytes")
        print(f"Tamano comprimido: {os.path.getsize(nombre_zip)} bytes")
        
    except Exception as e:
        print(f"Error al comprimir: {e}")

def descomprimir_archivo():
    ruta_zip = input("Ingrese la ruta del archivo ZIP: ").strip()
    
    if not os.path.exists(ruta_zip):
        print("El archivo ZIP no existe")
        return
    
    carpeta_destino = input("Ingrese carpeta de destino (Enter para carpeta actual): ").strip()
    if not carpeta_destino:
        carpeta_destino = "."
    
    try:
        with zipfile.ZipFile(ruta_zip, 'r') as zip_file:
            zip_file.extractall(carpeta_destino)
            archivos_extraidos = zip_file.namelist()
        
        print(f"Archivos extraidos exitosamente en: {carpeta_destino}")
        print("Archivos extraidos:")
        for archivo in archivos_extraidos:
            print(f"  - {archivo}")
            
    except Exception as e:
        print(f"Error al descomprimir: {e}")

def listar_contenido_zip():
    ruta_zip = input("Ingrese la ruta del archivo ZIP: ").strip()
    
    if not os.path.exists(ruta_zip):
        print("El archivo ZIP no existe")
        return
    
    try:
        with zipfile.ZipFile(ruta_zip, 'r') as zip_file:
            archivos = zip_file.infolist()
            print(f"\nContenido del archivo: {ruta_zip}")
            print("-" * 50)
            for info in archivos:
                print(f"Archivo: {info.filename}")
                print(f"Tamano original: {info.file_size} bytes")
                print(f"Tamano comprimido: {info.compress_size} bytes")
                print(f"Fecha: {info.date_time}")
                print("-" * 30)
                
    except Exception as e:
        print(f"Error al leer ZIP: {e}")

def proceso_completo():
    print("=== PROCESO COMPLETO: DESCARGAR, COMPRIMIR Y DESCOMPRIMIR ===")
    
    imagen = descargar_imagen_url()
    if not imagen:
        return
    
    nombre_zip = "imagen_procesada.zip"
    
    try:
        with zipfile.ZipFile(nombre_zip, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            zip_file.write(imagen, os.path.basename(imagen))
        
        print(f"\nImagen comprimida en: {nombre_zip}")
        
        carpeta_extraccion = "imagenes_extraidas"
        os.makedirs(carpeta_extraccion, exist_ok=True)
        
        with zipfile.ZipFile(nombre_zip, 'r') as zip_file:
            zip_file.extractall(carpeta_extraccion)
            archivos_extraidos = zip_file.namelist()
        
        print(f"Imagen descomprimida en: {carpeta_extraccion}")
        print("Proceso completo terminado exitosamente")
        
    except Exception as e:
        print(f"Error en proceso completo: {e}")

while True:
    print("\n=== GESTOR DE COMPRESION DE IMAGENES ===")
    print("1. Comprimir imagen")
    print("2. Descomprimir archivo ZIP")
    print("3. Listar contenido de ZIP")
    print("4. Proceso completo (descargar, comprimir, descomprimir)")
    print("5. Solo descargar imagen desde URL")
    print("6. Salir")
    
    opcion = input("Seleccione una opcion: ").strip()
    
    if opcion == "1":
        comprimir_imagen()
    elif opcion == "2":
        descomprimir_archivo()
    elif opcion == "3":
        listar_contenido_zip()
    elif opcion == "4":
        proceso_completo()
    elif opcion == "5":
        descargar_imagen_url()
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opcion no valida")