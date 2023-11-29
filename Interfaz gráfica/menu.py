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

        #Cantidad de columnas y filas
        self.columnconfigure(3, weight = 5)
        self.rowconfigure(3, weight = 5)

        #Imagenes
        self.signo_exclamacion = customtkinter.CTkImage(Image.open(os.path.join(image_path,'signoExclamacion.png')), size = (100, 50))

        self.frame = CTkFrame(self, fg_color = c_blanco)
        self.frame.grid(column = 3, row = 3, sticky = 'nsew')

        #Texto Menú
        self.texto_menu = customtkinter.CTkLabel(master = self, width=200, height = 100, corner_radius=0, font = ('sans rerif', 75), 
                                                   fg_color = c_blanco, bg_color = c_blanco, text_color = c_negro, text = "Menú")
        self.texto_menu.place(relx = 0.425, rely = 0.05) 

        #Signo de exclamacion y posicion
        self.signo_exclamacion = customtkinter.CTkLabel(self, image = self.signo_exclamacion, text = '', fg_color = c_blanco)
        self.signo_exclamacion.place(relx = 0.1, rely = 0.1, anchor = tkinter.NE)

        #Boton Ajustar sistema
        self.bt_ajustar = CTkButton(self, font = customtkinter.CTkFont('sans rerif', 20), border_color = c_negro, border_width = 3,
                hover_color = c_gris, fg_color = c_blanco, text = 'Ajustar sistema', height = 80, width = 250, text_color = c_negro)
        self.bt_ajustar.place(relx = 0.5, rely = 0.3, anchor = tkinter.CENTER)

        #Boton Contactos de emergencia
        self.bt_contactos = CTkButton(self, font = customtkinter.CTkFont('sans rerif', 20), border_color = c_negro, border_width = 3,
                hover_color = c_gris, fg_color = c_blanco, text = 'Contactos de emergencia', height = 80, width = 250, text_color = c_negro)
        self.bt_contactos.place(relx = 0.5, rely = 0.45, anchor = tkinter.CENTER)

        #Boton Historial de actividad
        self.bt_historial = CTkButton(self, font = customtkinter.CTkFont('sans rerif', 20), border_color = c_negro, border_width = 3,
                hover_color = c_gris, fg_color = c_blanco, text = 'Historial de actividad', height = 80, width = 250, text_color = c_negro)
        self.bt_historial.place(relx = 0.5, rely = 0.6, anchor = tkinter.CENTER)

        #Boton Calidad del aire
        self.bt_caldiad = CTkButton(self, font = customtkinter.CTkFont('sans rerif', 20), border_color = c_negro, border_width = 3,
                hover_color = c_gris, fg_color = c_blanco, text = 'Calidad del aire', height = 80, width = 250, text_color = c_negro)
        self.bt_caldiad.place(relx = 0.5, rely = 0.75, anchor = tkinter.CENTER)

        #Boton Perfil
        self.bt_perfil = CTkButton(self, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, border_width = 3,
                hover_color = c_gris, fg_color = c_blanco, text = 'Perfil', height = 20, width = 100, text_color = c_negro)
        self.bt_perfil.place(relx = 0.9, rely = 0.1, anchor = tkinter.CENTER)

        #Boton Cerrar sesión
        self.bt_cerrar = CTkButton(self, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, border_width = 3,
                hover_color = c_gris, fg_color = c_blanco, text = 'Cerrar sesión', height = 20, width = 100, text_color = c_negro)
        self.bt_cerrar.place(relx = 0.9, rely = 0.15, anchor = tkinter.CENTER)

menu = menu()

def mostrarMenu():
        menu.mainloop()
mostrarMenu()