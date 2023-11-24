from customtkinter import *
from tkinter import PhotoImage
import customtkinter
import os
import tkinter
from PIL import Image

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'images')

c_blanco = '#FFFFFF'
c_negro = '#010101'
c_morado = '#7f5aF0'
c_verde = '#2cb67d'
c_calipso = '#69f9ec'
c_naranjo = '#FF8000'
c_azul = '#0000FF'

#Inicio de sesion
root = CTk()
root.geometry('1280x720')
root.minsize(1280,720)
root.config(bg = c_blanco)
root.title('S.A.I.I')

#Texto iniciar sesion
'''
text = label.cget("text")
'''

#Imagenes
signo_exclamacion = customtkinter.CTkImage(Image.open(os.path.join(image_path,'signoExclamacion.png')), size = (300, 250))

frame = CTkFrame(root, fg_color = c_blanco)
frame.grid(column = 3, row = 3, sticky = 'nsew')

root.columnconfigure(3, weight = 5)
root.rowconfigure(3, weight = 5)

#Signo de exclamacion y posicion
signo_exclamacion = customtkinter.CTkLabel(frame, image = signo_exclamacion, text = '')
signo_exclamacion.place(relx = 0.6, rely = 0.3, anchor = tkinter.NE)

#Boton detener
bt_detener = CTkButton(frame, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, border_width = 2,
          hover_color = c_naranjo, fg_color = 'transparent', text = 'Detener', height = 60, text_color = c_negro)
bt_detener.place(relx = 0.54, rely = 0.8, anchor = tkinter.NE)

root.mainloop()