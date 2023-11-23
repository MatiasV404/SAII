from customtkinter import CTk, CTkFrame, CTkEntry, CTkLabel, CTkButton, CTkCheckBox, CTkImage
from tkinter import PhotoImage
import customtkinter
import os
import tkinter

image = None
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Fotos")

c_blanco = '#FFFFFF'
c_negro = '#010101'
c_morado = '#7f5aF0'
c_verde = '#2cb67d'
c_calipso = '#69f9ec'
c_naranjo = '#FF8000'

#Inicio de sesion

root = CTk()
root.geometry('1280x720+320+180')
root.minsize(1280,720)
root.config(bg = c_blanco)
root.title('Inicio de sesion')

logo_llama = PhotoImage(file = 'images/llama.png') 

frame = CTkFrame(root, fg_color = c_blanco)
frame.grid(column = 3, row = 3, sticky = 'nsew', padx = 50, pady = 50)

root.columnconfigure(3, weight = 5)
root.rowconfigure(3, weight = 5)

#Logo y posicion
CTkLabel(frame, image = logo_llama).place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER) 

#Entrada correo y contraseña
correo = CTkEntry(frame, font = ('sans rerif', 12), placeholder_text = 'Correo electronico',
                  border_color = c_blanco, fg_color = c_blanco, width = 220, height = 40)
correo.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

contrasenia = CTkEntry(frame, font = ('sans rerif', 12), placeholder_text = 'Contraseña',
                  border_color = c_blanco, fg_color = c_blanco, width = 220, height = 40)
contrasenia.place(relx = 0.5, rely = 0.6, anchor = tkinter.CENTER)

#Recordar contraseña
checkbox = CTkCheckBox(frame, text = '¿Olvidaste tu contraseña?', hover_color = c_naranjo,
                       border_color = c_blanco, fg_color = c_naranjo)
checkbox.place(relx = 0.5, rely = 0.7, anchor = tkinter.CENTER)

#Boton ingresar
bt_ingresar = CTkButton(frame, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_blanco, fg_color = c_blanco,
          hover_color = c_naranjo, text = 'Ingresar', height = 40, text_color = c_negro)
bt_ingresar.place(relx = 0.5, rely = 0.8, anchor = tkinter.CENTER)

root.call('wm', 'iconphoto', root._w, logo_llama)
root.mainloop()
