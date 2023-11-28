import os
from PIL import Image
import customtkinter
from customtkinter import *
import tkinter
from tkinter import PhotoImage

class alarmaActivada(customtkinter.CTk):
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
        self.config(bg = c_blanco)
        self.title('S.A.I.I')

        #Cantidad de columnas y filas
        self.columnconfigure(3, weight = 5)
        self.rowconfigure(3, weight = 5)

        #Imagenes
        self.signo_exclamacion = customtkinter.CTkImage(Image.open(os.path.join(image_path,'signoExclamacion.png')), size = (100, 50))
        self.frame = CTkFrame(self, fg_color = c_blanco)
        self.frame.grid(column = 3, row = 3, sticky = 'nsew')
        
        #Texto Alarma activada
        self.alarma_activada = customtkinter.CTkLabel(self, width=650, height = 10, font = ('sans rerif', 75), fg_color = c_blanco,
                                                        bg_color = c_blanco, text_color = c_negro, text = "Alarma activada")
        self.alarma_activada.place(relx = 0.25, rely = 0.1) 

        #Signo de exclamacion y posicion
        self.signo_exclamacion = customtkinter.CTkLabel(self, image = self.signo_exclamacion, text = '', fg_color = c_blanco)
        self.signo_exclamacion.place(relx = 0.3, rely = 0.5, anchor = tkinter.CENTER)
        
        #Signo de exclamacion y posicion
        self.signo_exclamacion = customtkinter.CTkLabel(self, image = self.signo_exclamacion, text = '', fg_color = c_blanco)
        self.signo_exclamacion.place(relx = 0.6, rely = 0.4, anchor = tkinter.NE)

        #Boton detener
        self.bt_detener = CTkButton(self, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, border_width = 2,
                hover_color = c_gris, fg_color = c_blanco, text = 'Detener', height = 60, text_color = c_negro)
        self.bt_detener.place(relx = 0.57, rely = 0.8, anchor = tkinter.NE)

alarmaActivada = alarmaActivada()
alarmaActivada.mainloop()