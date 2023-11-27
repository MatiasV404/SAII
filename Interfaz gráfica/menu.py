from customtkinter import *
from tkinter import PhotoImage
import customtkinter
import os
import tkinter
from PIL import Image

class menu(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'images')

        c_blanco = '#FFFFFF'
        c_negro = '#010101'
        c_morado = '#7f5aF0'
        c_verde = '#2cb67d'
        c_calipso = '#69f9ec'
        c_gris_oscuro = '#424949'
        c_azul = '#0000FF'
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

        #Texto Menú
        self.texto_iniciar = customtkinter.CTkTextbox(master = self, width=200, height = 100, corner_radius=0, font = ('sans rerif', 75), fg_color = c_blanco,
                                                      text_color = c_negro)
        self.texto_iniciar.place(relx = 0.43, rely = 0.05) 
        self.texto_iniciar.insert("0.0", "Menú" * 1)
        self.texto_iniciar.configure(state = DISABLED)

        #Signo de exclamacion y posicion
        self.signo_exclamacion = customtkinter.CTkLabel(self, image = self.signo_exclamacion, text = '', fg_color = c_blanco)
        self.signo_exclamacion.place(relx = 0.1, rely = 0.1, anchor = tkinter.NE)

        #Boton Ajustar sistema
        self.bt_ingresar = CTkButton(self, font = customtkinter.CTkFont('sans rerif', 15), border_color = c_negro, border_width = 3,
                hover_color = c_gris, fg_color = c_blanco, text = 'Ajustar sistema', height = 80, width = 250, text_color = c_negro)
        self.bt_ingresar.place(relx = 0.5, rely = 0.3, anchor = tkinter.CENTER)

        #Boton Contactos de emergencia
        self.bt_ingresar = CTkButton(self, font = customtkinter.CTkFont('sans rerif', 15), border_color = c_negro, border_width = 3,
                hover_color = c_gris, fg_color = c_blanco, text = 'Contactos de emergencia', height = 80, width = 250, text_color = c_negro)
        self.bt_ingresar.place(relx = 0.5, rely = 0.45, anchor = tkinter.CENTER)

        #Boton Historial de actividad
        self.bt_ingresar = CTkButton(self, font = customtkinter.CTkFont('sans rerif', 15), border_color = c_negro, border_width = 3,
                hover_color = c_gris, fg_color = c_blanco, text = 'Historial de actividad', height = 80, width = 250, text_color = c_negro)
        self.bt_ingresar.place(relx = 0.5, rely = 0.6, anchor = tkinter.CENTER)

        #Boton Calidad del aire
        self.bt_ingresar = CTkButton(self, font = customtkinter.CTkFont('sans rerif', 15), border_color = c_negro, border_width = 3,
                hover_color = c_gris, fg_color = c_blanco, text = 'Calidad del aire', height = 80, width = 250, text_color = c_negro)
        self.bt_ingresar.place(relx = 0.5, rely = 0.75, anchor = tkinter.CENTER)

        #Boton Perfil
        self.bt_ingresar = CTkButton(self, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, border_width = 3,
                hover_color = c_gris, fg_color = c_blanco, text = 'Perfil', height = 20, width = 100, text_color = c_negro)
        self.bt_ingresar.place(relx = 0.9, rely = 0.1, anchor = tkinter.CENTER)

        #Boton Cerrar sesión
        self.bt_ingresar = CTkButton(self, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, border_width = 3,
                hover_color = c_gris, fg_color = c_blanco, text = 'Cerrar sesión', height = 20, width = 100, text_color = c_negro)
        self.bt_ingresar.place(relx = 0.9, rely = 0.15, anchor = tkinter.CENTER)

menu = menu()
menu.mainloop()