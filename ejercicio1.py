from PIL import Image
import os

print("ingrese la ubicacion del archivo")
url = input()
img = Image.open(url) 
img.show()
nombreArchivo = os.path.basename(url)
nombre, extension = os.path.splitext(url)
resolucion = img.size
cantidad_pixel = resolucion[0] * resolucion[1]

print(f"El nombre del archivo es: {nombreArchivo}")
print(f"La extension de la imagen es: {extension}")
print(f"La resolucion de la imagen es {resolucion[0]}px por {resolucion[1]}px")
print(f"La cantidad de pixeles de la imagen es de {cantidad_pixel}")