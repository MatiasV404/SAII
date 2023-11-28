import os
from PIL import Image
import customtkinter
from customtkinter import *
import tkinter
from tkinter import PhotoImage

class historial(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'images')

        c_blanco = '#FFFFFF'
        c_negro = '#010101'
        c_gris_oscuro = '#424949'
        c_azul = '#0000FF'
        c_gris = '#979A9A'

        #Historial de actividad
        self.geometry('1280x720')
        self.minsize(1280,720)
        self.maxsize(1280,720)
        self.title('S.A.I.I')

        #Imagenes
        self.signo_exclamacion = customtkinter.CTkImage(Image.open(os.path.join(image_path,'signoExclamacion.png')), size = (100, 50))
        self.frame = CTkFrame(self, fg_color = c_blanco)
        self.frame.grid(column = 3, row = 3, sticky = 'nsew')

        #Columnas y filas
        self.columnconfigure(3, weight = 5)
        self.rowconfigure(3, weight = 5)
        
        #Texto Contactos de emergencia
        self.texto_contactos_emergencia = customtkinter.CTkLabel(master = self, width=300, height = 100, font = ('sans rerif', 50), fg_color = c_blanco,
                                                      text_color = c_negro, text = "Contactos de emergencia")
        self.texto_contactos_emergencia.place(relx = 0.27, rely = 0.05)

        #Signo de exclamacion y posicion
        self.signo_exclamacion = customtkinter.CTkLabel(self, image = self.signo_exclamacion, text = '', fg_color = c_blanco)
        self.signo_exclamacion.place(relx = 0.1, rely = 0.1, anchor = tkinter.NE)

        #Boton Volver
        self.bt_volver = CTkButton(self, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, border_width = 3,
                hover_color = c_gris, fg_color = c_blanco, text = 'Volver', height = 20, width = 100, text_color = c_negro)
        self.bt_volver.place(relx = 0.9, rely = 0.1, anchor = tkinter.CENTER)

        #Tabla historial de actividad
        self.tab_historial_actividad = customtkinter.CTkTabview(self, width = 550, height = 450, border_width = 2, fg_color = c_blanco)
        self.tab_historial_actividad.place(relx = 0.5, rely = 0.3)

        #Boton Eliminar contacto
        self.bt_eliminar_contacto = CTkButton(self.frame, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, border_width = 2,
                hover_color = c_gris, fg_color = 'transparent', text = 'Eliminar contacto', height = 40, width = 200, text_color = c_negro)
        self.bt_eliminar_contacto.place(relx = 0.25, rely = 0.7, anchor = tkinter.CENTER)

        #Ingrese el correo electrónico
        self.correo_electronico = CTkEntry(self, font = ('sans rerif', 12), placeholder_text = '', text_color = c_negro,
                        border_color = c_negro, fg_color = c_blanco, width = 380, height = 40)
        self.correo_electronico.place(relx = 0.2, rely = 0.5, anchor = tkinter.CENTER)

        #Boton Agregar contacto
        self.bt_agregar_contacto = CTkButton(self.frame, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, border_width = 2,
                hover_color = c_gris, fg_color = 'transparent', text = 'Agregar', height = 40, width = 75, text_color = c_negro)
        self.bt_agregar_contacto.place(relx = 0.4, rely = 0.5, anchor = tkinter.CENTER)

        #Texto Ingreso el correo electrónico
        self.correo_electronico = customtkinter.CTkLabel(master = self, width = 200, height = 30, corner_radius=0, font = ('sans rerif', 15), fg_color = c_blanco,
                                                    text_color = c_negro, text = "Ingreso el correo electrónico")
        self.correo_electronico.place(relx = 0.05, rely = 0.43) 

historial = historial()
historial.mainloop()
