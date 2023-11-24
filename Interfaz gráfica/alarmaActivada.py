from customtkinter import *
from tkinter import PhotoImage
import customtkinter
import os
import tkinter
from PIL import Image

class alarmaActivada(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'images')

        c_blanco = '#FFFFFF'
        c_negro = '#010101'
        c_morado = '#7f5aF0'
        c_verde = '#2cb67d'
        c_calipso = '#69f9ec'
        c_naranjo = '#FF8000'
        c_azul = '#0000FF'

        #Inicio de sesion
        self.geometry('1280x720')
        self.minsize(1280,720)
        self.config(bg = c_blanco)
        self.title('S.A.I.I')

        #Texto Alarma activada
        self.alarma_activada = customtkinter.CTkTextbox(master = self, width=650, height = 10, font = ('sans rerif', 75), fg_color = c_blanco,
                                                        bg_color = c_blanco, text_color = c_negro)
        self.alarma_activada.place(relx = 0.3, rely = 0.1) 
        self.alarma_activada.insert("0.0", "¡Alarma Activada!" * 1)
        self.alarma_activada.configure(state = DISABLED)

        #Imagenes
        self.signo_exclamacion = customtkinter.CTkImage(Image.open(os.path.join(image_path,'signoExclamacion.png')), size = (200, 150))

        self.frame = CTkFrame(self, fg_color = c_blanco)
        self.frame.grid(column = 1, row = 1, sticky = 'nsew')

        #Cantidad de columnas y filas
        self.columnconfigure(5, weight = 1)
        self.rowconfigure(5, weight = 1)

        #Signo de exclamacion y posicion
        self.signo_exclamacion = customtkinter.CTkLabel(self, image = self.signo_exclamacion, text = '', fg_color = c_blanco)
        self.signo_exclamacion.place(relx = 0.6, rely = 0.3, anchor = tkinter.NE)

        #Boton detener
        self.bt_detener = CTkButton(self.frame, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, border_width = 2,
                hover_color = c_naranjo, fg_color = 'transparent', text = 'Detener', height = 60, text_color = c_negro)
        self.bt_detener.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

alarmaActivada = alarmaActivada()
alarmaActivada.mainloop()