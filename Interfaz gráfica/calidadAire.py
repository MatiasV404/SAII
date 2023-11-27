import os
from PIL import Image
import customtkinter
from customtkinter import *
import tkinter
from tkinter import PhotoImage

class menu(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'images')

        c_blanco = '#FFFFFF'
        c_negro = '#010101'
        c_gris = '#979A9A'

        #Inicio de sesion
        self.geometry('1280x720')
        self.minsize(1280,720)
        self.maxsize(1280,720)
        self.title('S.A.I.I')

         #Imagenes
        self.signo_exclamacion = customtkinter.CTkImage(Image.open(os.path.join(image_path,'signoExclamacion.png')), size = (100, 50))

        self.frame = CTkFrame(self, fg_color = c_blanco)
        self.frame.grid(column = 3, row = 3, sticky = 'nsew')

        self.columnconfigure(3, weight = 5)
        self.rowconfigure(3, weight = 5)

        #Texto Calidad del aire
        self.texto_iniciar = customtkinter.CTkTextbox(master = self, width=700, height = 100, corner_radius=0, font = ('sans rerif', 50), fg_color = c_blanco,
                                                      text_color = c_negro)
        self.texto_iniciar.place(relx = 0.35, rely = 0.05) 
        self.texto_iniciar.insert("0.0", "Calidad del Aire" * 1)
        self.texto_iniciar.configure(state = DISABLED)

        #Texto Subtitulo
        self.texto_iniciar = customtkinter.CTkTextbox(master = self, width=700, height = 100, corner_radius=0, font = ('sans rerif', 50), fg_color = c_blanco,
                                                      text_color = c_negro)
        self.texto_iniciar.place(relx = 0.35, rely = 0.05) 
        self.texto_iniciar.insert("0.0", "Calidad del Aire" * 1)
        self.texto_iniciar.configure(state = DISABLED)

        #Signo de exclamacion y posicion
        self.signo_exclamacion = customtkinter.CTkLabel(self, image = self.signo_exclamacion, text = '', fg_color = c_blanco)
        self.signo_exclamacion.place(relx = 0.1, rely = 0.1, anchor = tkinter.NE)

menu = menu()
menu.mainloop()