import os 

'''
#Obtener ruta
ruta_actual = os.path.abspath(__file__)

#navegar
ruta_vista_bd = os.path.abspath(os.path.join(ruta_actual, "..", ".."))

#Importar imagen
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'images')

print(ruta_actual)
print(ruta_vista_bd)
print(image_path)
'''

'''
from PIL import Image
from customtkinter import *

my_image = customtkinter.CTkImage(light_image=Image.open("<path to light mode image>"),
                                  dark_image=Image.open("<path to dark mode image>"),
                                  size=(30, 30))

image_label = customtkinter.CTkLabel(app, image=my_image, text="")  # display image with a CTkLabel
'''