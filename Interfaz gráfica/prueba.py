from customtkinter import CTk, CTkFrame, CTkEntry, CTkLabel, CTkButton, CTkCheckBox, CTkImage
from tkinter import PhotoImage
import customtkinter
import os
import tkinter

image = None
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Fotos")

c_negro = '#010101'
c_morado = '#7f5aF0'
c_verde = '#2cb67d'
c_calipso = '#8CBED6'

#Inicio de sesion

root = CTk()
root.geometry('500x600+350+20')
root.minsize(480,500)
root.config(bg = c_negro)
root.title('Inicio de sesion')

logo_llama = tkinter.PhotoImage(file = 'images/llama.png') 

frame = CTkFrame(root, fg_color = c_calipso)
frame.grid(column = 0, row = 0, sticky = 'nsew', padx = 50, pady = 50)

root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

#Logo y posicion
CTkLabel(root, image = logo_llama).grid(columnspan = 2, row = 0) 

#Entrada correo y contraseña
correo = CTkEntry(root, font = ('sans rerif', 12), placeholder_text = 'Correo electronico',
                  border_color = c_morado, fg_color = c_negro, width = 220, height = 40)
correo.grid(columnspan = 2, row = 1, padx = 4, pady = 4)

contrasenia = CTkEntry(root, font = ('sans rerif', 12), placeholder_text = 'Contraseña',
                  border_color = c_morado, fg_color = c_negro, width = 220, height = 40)
contrasenia.grid(columnspan = 2, row = 2, padx = 4, pady = 4)

checkbox = CTkCheckbox 

root.call('wm', 'iconphoto', root._w, logo_llama)
root.mainloop()
