import os
from PIL import Image
import customtkinter
from customtkinter import *
import tkinter
from tkinter import PhotoImage

class configuracion(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'images')

        c_blanco = '#FFFFFF'
        c_negro = '#010101'
        c_gris_oscuro = '#424949'
        c_gris = '#979A9A'

        #Ajustar sistema
        self.geometry('1280x720')
        self.minsize(1280,720)
        self.maxsize(1280,720)
        self.title('S.A.I.I')

        self.signo_exclamacion = customtkinter.CTkImage(Image.open(os.path.join(image_path,'signoExclamacion.png')), size = (100, 50))

        self.frame = CTkFrame(self, fg_color = c_blanco)
        self.frame.grid(column = 3, row = 3, sticky = 'nsew')

        self.columnconfigure(3, weight = 5)
        self.rowconfigure(3, weight = 5)
        
        #Signo de exclamacion y posicion
        self.signo_exclamacion = customtkinter.CTkLabel(self.frame, image = self.signo_exclamacion, text = '')
        self.signo_exclamacion.place(relx = 0.1, rely = 0.1, anchor = tkinter.NE)
        
        #Texto Ajustar sistema
        self.texto_ajustar = customtkinter.CTkTextbox(master = self, width = 600, height = 100, corner_radius=0, font = ('sans rerif', 75), fg_color = c_blanco,
                                                    text_color = c_negro)
        self.texto_ajustar.place(relx = 0.3, rely = 0.05) 
        self.texto_ajustar.insert("0.0", "Ajustar sistema" * 1)
        self.texto_ajustar.configure(state = DISABLED)

        #Texto Volúmen buzzers
        self.texto_volumen = customtkinter.CTkTextbox(master = self, width = 130, height = 50, corner_radius=0, font = ('sans rerif', 15), fg_color = c_blanco,
                                                    text_color = c_negro)
        self.texto_volumen.place(relx = 0.075, rely = 0.475) 
        self.texto_volumen.insert("0.0", "Volúmen buzzers" * 1)
        self.texto_volumen.configure(state = DISABLED)

        #Texto Duración de alarma
        self.texto_duracion = customtkinter.CTkTextbox(master = self, width = 130, height = 50, corner_radius=0, font = ('sans rerif', 15), fg_color = c_blanco,
                                                    text_color = c_negro)
        self.texto_duracion.place(relx = 0.075, rely = 0.675) 
        self.texto_duracion.insert("0.0", "Duración alarma" * 1)
        self.texto_duracion.configure(state = DISABLED)

        #Texto Fuentes de letras
        self.texto_fuente = customtkinter.CTkTextbox(master = self, width = 130, height = 50, corner_radius=0, font = ('sans rerif', 15), fg_color = c_blanco,
                                                    text_color = c_negro)
        self.texto_fuente.place(relx = 0.425, rely = 0.475) 
        self.texto_fuente.insert("0.0", "Fuentes de letras" * 1)
        self.texto_fuente.configure(state = DISABLED)

        #Texto Sistema de sensores
        self.texto_sensores = customtkinter.CTkTextbox(master = self, width = 150, height = 50, corner_radius=0, font = ('sans rerif', 15), fg_color = c_blanco,
                                                    text_color = c_negro)
        self.texto_sensores.place(relx = 0.760, rely = 0.275) 
        self.texto_sensores.insert("0.0", "Sistema de sensores" * 1)
        self.texto_sensores.configure(state = DISABLED)
        
        #Boton Probar sonido
        self.bt_probar_sonido = CTkButton(self.frame, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, border_width = 2,
                hover_color = c_gris, fg_color = 'transparent', text = 'Probar sonido', height = 20, width = 200, text_color = c_negro)
        self.bt_probar_sonido.place(relx = 0.15, rely = 0.3, anchor = tkinter.CENTER)

        #Boton Configurar parpadeo LED
        self.bt_configurar_parpadeo = CTkButton(self.frame, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, border_width = 2,
                hover_color = c_gris, fg_color = 'transparent', text = 'Configurar parpadeo LED', height = 20, width = 200, text_color = c_negro)
        self.bt_configurar_parpadeo.place(relx = 0.5, rely = 0.3, anchor = tkinter.CENTER)

        #Boton Volver
        self.bt_volver = CTkButton(self.frame, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, border_width = 2,
                hover_color = c_gris, fg_color = 'transparent', text = 'Volver', height = 30, text_color = c_negro)
        self.bt_volver.place(relx = 0.9, rely = 0.1, anchor = tkinter.CENTER)

        #Boton Guardar cambios
        self.bt_guardar_cambios = CTkButton(self.frame, font = customtkinter.CTkFont('sans rerif', 15), border_color = c_negro, border_width = 2,
                hover_color = c_gris, fg_color = 'transparent', text = 'Guardar cambios', height = 60, width = 180, text_color = c_negro)
        self.bt_guardar_cambios.place(relx = 0.5, rely = 0.9, anchor = tkinter.CENTER)

        #Boton Modificar PIN de seguridad
        self.bt_modificar_pin = CTkButton(self.frame, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, border_width = 2,
                hover_color = c_gris, fg_color = 'transparent', text = 'Modificar PIN de seguridad', height = 20, width = 200, text_color = c_negro)
        self.bt_modificar_pin.place(relx = 0.5, rely = 0.7, anchor = tkinter.CENTER)

        #Boton Restablecer ajustes de fábrica
        self.bt_restablecer_ajustes = CTkButton(self.frame, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, border_width = 2,
                hover_color = c_gris, fg_color = 'transparent', text = 'Restablecer ajustes de fábrica', height = 20, width = 200, text_color = c_negro)
        self.bt_restablecer_ajustes.place(relx = 0.85, rely = 0.7, anchor = tkinter.CENTER)

        #ComboBox Volumen buzzers
        self.cb_volumen_buzzers = customtkinter.CTkComboBox(self.frame, values=["1", "2", "3"], border_color = c_negro, fg_color = c_blanco, button_color = c_gris_oscuro, button_hover_color = c_gris,
                                                    text_color = c_negro, dropdown_fg_color = c_blanco,dropdown_hover_color = c_gris, dropdown_text_color = c_negro, width = 50)
        self.cb_volumen_buzzers.place(relx = 0.2, rely = 0.5, anchor = tkinter.CENTER)

        #ComboBox Duracion de alarma
        self.cb_duracion_alarma = customtkinter.CTkComboBox(self.frame, values=["1", "2", "3"], border_color = c_negro, fg_color = c_blanco, button_color = c_gris_oscuro, button_hover_color = c_gris,
                                                    text_color = c_negro, dropdown_fg_color = c_blanco,dropdown_hover_color = c_gris, dropdown_text_color = c_negro, width = 50)
        self.cb_duracion_alarma.place(relx = 0.2, rely = 0.7, anchor = tkinter.CENTER)

        #ComboBox Fuente de las letras
        self.cb_fuente_letras = customtkinter.CTkComboBox(self.frame, values=["5", "10", "15","20"], border_color = c_negro, fg_color = c_blanco, button_color = c_gris_oscuro, button_hover_color = c_gris,
                                                    text_color = c_negro, dropdown_fg_color = c_blanco,dropdown_hover_color = c_gris, dropdown_text_color = c_negro, width = 55)
        self.cb_fuente_letras.place(relx = 0.55, rely = 0.5, anchor = tkinter.CENTER)

        #SwitchButton Sistema de sensores
        self.switch_var = customtkinter.StringVar(value="on")
        self.sw_sistema_sensores = customtkinter.CTkSwitch(self.frame, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, text = '',
                                                    variable = self.switch_var, text_color = c_negro, fg_color = c_gris, onvalue="on", offvalue="off")
        self.sw_sistema_sensores.place(relx = 0.93, rely = 0.3, anchor = tkinter.CENTER)

configuracion = configuracion()
configuracion.mainloop()