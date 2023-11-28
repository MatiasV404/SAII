import os
from PIL import Image
import customtkinter
from customtkinter import *
import tkinter
from tkinter import PhotoImage

class calidadAire(customtkinter.CTk):
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
        self.texto_calidad = customtkinter.CTkLabel(master = self, width=400, height = 100, corner_radius = 0, font = ('sans rerif', 50), fg_color = c_blanco,
                                                      text_color = c_negro, bg_color = c_blanco, text = "Calidad del Aire")
        self.texto_calidad.place(relx = 0.35, rely = 0.05) 

        #Texto Subtitulo
        self.texto_subtitulo = customtkinter.CTkLabel(master = self, width=1000, height = 100, corner_radius=0, font = ('sans rerif', 30), fg_color = c_blanco,
                                                      bg_color = c_blanco, text_color = c_negro, text = "A continuaión se muestran los niveles de concentración de:")
        self.texto_subtitulo.place(relx = 0.15, rely = 0.25) 

        #Textbox Valor Humo
        self.textbox_valor_humo = customtkinter.CTkTextbox(self, width=80, height = 30, corner_radius=0, font = ('sans rerif', 20), fg_color = c_blanco,
                                                      text_color = c_negro, border_color = c_negro, border_width = 2)
        self.textbox_valor_humo.place(relx = 0.55, rely = 0.4) 
        self.textbox_valor_humo.insert("0.0", "   x%" * 1)
        self.textbox_valor_humo.configure(state = DISABLED)

        #Texto Humo
        self.texto_humo = customtkinter.CTkLabel(self, width=80, height = 30, corner_radius = 0, font = ('sans rerif', 20), fg_color = c_blanco, 
                                                 bg_color = c_blanco, text_color = c_negro, text = "Humo", anchor = SW)
        self.texto_humo.place(relx = 0.45, rely = 0.4) 

        #Textbox Valor Benceno
        self.textbox_valor_benceno = customtkinter.CTkTextbox(self, width=80, height = 30, corner_radius=0, font = ('sans rerif', 20), fg_color = c_blanco,
                                                      text_color = c_negro, border_color = c_negro, border_width = 2)
        self.textbox_valor_benceno.place(relx = 0.55, rely = 0.47) 
        self.textbox_valor_benceno.insert("0.0", "   x%" * 1)
        self.textbox_valor_benceno.configure(state = DISABLED)

        #Texto Benceno
        self.texto_benceno = customtkinter.CTkLabel(self, width=80, height = 30, corner_radius = 0, font = ('sans rerif', 20), fg_color = c_blanco,
                                                    bg_color = c_blanco, text_color = c_negro, text = "Benceno", anchor = SW)
        self.texto_benceno.place(relx = 0.45, rely = 0.47) 

        #Textbox Valor Amoniaco (NH3)
        self.textbox_valor_amoniaco = customtkinter.CTkTextbox(self, width=80, height = 30, corner_radius=0, font = ('sans rerif', 20), fg_color = c_blanco,
                                                      text_color = c_negro, border_color = c_negro, border_width = 2)
        self.textbox_valor_amoniaco.place(relx = 0.55, rely = 0.54) 
        self.textbox_valor_amoniaco.insert("0.0", "   x%" * 1)
        self.textbox_valor_amoniaco.configure(state = DISABLED)

        #Texto Amoniaco
        self.texto_amoniaco = customtkinter.CTkLabel(self, width=80, height = 30, corner_radius = 0, font = ('sans rerif', 20), fg_color = c_blanco, text_color = c_negro, text = "NH3", 
                                                     anchor = SW)
        self.texto_amoniaco.place(relx = 0.45, rely = 0.54) 

        #Textbox Valor Dioxido de Carbono (CO2)
        self.textbox_valor_dioxido = customtkinter.CTkTextbox(self, width=80, height = 30, corner_radius=0, font = ('sans rerif', 20), fg_color = c_blanco,
                                                      text_color = c_negro, border_color = c_negro, border_width = 2)
        self.textbox_valor_dioxido.place(relx = 0.55, rely = 0.61) 
        self.textbox_valor_dioxido.insert("0.0", "   x%" * 1)
        self.textbox_valor_dioxido.configure(state = DISABLED)

        #Texto Dioxido de Carbono (CO2)
        self.texto_dioxido = customtkinter.CTkLabel(self, width=80, height = 30, corner_radius = 0, font = ('sans rerif', 20), fg_color = c_blanco, text_color = c_negro, text = "CO2", 
                                                    anchor = SW)
        self.texto_dioxido.place(relx = 0.45, rely = 0.61) 

        #Textbox Valor NOx 
        self.textbox_valor_nox = customtkinter.CTkTextbox(self, width=80, height = 30, corner_radius=0, font = ('sans rerif', 20), fg_color = c_blanco,
                                                      text_color = c_negro, border_color = c_negro, border_width = 2)
        self.textbox_valor_nox.place(relx = 0.55, rely = 0.68) 
        self.textbox_valor_nox.insert("0.0", "   x%" * 1)
        self.textbox_valor_nox.configure(state = DISABLED)

        #Texto NOX
        self.texto_nox = customtkinter.CTkLabel(self, width=80, height = 30, corner_radius = 0, font = ('sans rerif', 20), fg_color = c_blanco, text_color = c_negro, text = "NOX", 
                                                anchor = SW)
        self.texto_nox.place(relx = 0.45, rely = 0.68) 

        #Textbox Valor Alcohol 
        self.textbox_valor_alcohol = customtkinter.CTkTextbox(self, width=80, height = 30, corner_radius=0, font = ('sans rerif', 20), fg_color = c_blanco,
                                                      text_color = c_negro, border_color = c_negro, border_width = 2)
        self.textbox_valor_alcohol.place(relx = 0.55, rely = 0.75) 
        self.textbox_valor_alcohol.insert("0.0", "   x%" * 1)
        self.textbox_valor_alcohol.configure(state = DISABLED)

        #Texto Alcohol
        self.texto_alcohol = customtkinter.CTkLabel(self, width=80, height = 30, corner_radius = 0, font = ('sans rerif', 20), fg_color = c_blanco, text_color = c_negro, text = "Alcohol", 
                                                    anchor = SW)
        self.texto_alcohol.place(relx = 0.45, rely = 0.75) 

        #Boton Volver
        self.bt_volver = CTkButton(self, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, border_width = 3,
                hover_color = c_gris, fg_color = c_blanco, text = 'Volver', height = 20, width = 100, text_color = c_negro)
        self.bt_volver.place(relx = 0.9, rely = 0.1, anchor = tkinter.CENTER)

        #Signo de exclamacion y posicion
        self.signo_exclamacion = customtkinter.CTkLabel(self, image = self.signo_exclamacion, text = '', fg_color = c_blanco)
        self.signo_exclamacion.place(relx = 0.1, rely = 0.1, anchor = tkinter.NE)

calidadAire = calidadAire()
calidadAire.mainloop()