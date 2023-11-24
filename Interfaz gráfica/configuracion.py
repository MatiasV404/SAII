from customtkinter import *
from tkinter import PhotoImage
import customtkinter
import os
import tkinter
from PIL import Image

class configuracion(customtkinter.CTk):
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

        #Ajustar sistema
        self.geometry('1280x720')
        self.minsize(1280,720)
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
        
        #Boton Probar sonido
        self.bt_probar_sonido = CTkButton(self.frame, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, border_width = 2,
                hover_color = c_naranjo, fg_color = 'transparent', text = 'Probar sonido', height = 20, text_color = c_negro)
        self.bt_probar_sonido.place(relx = 0.1, rely = 0.3, anchor = tkinter.CENTER)

        #Boton Configurar parpadeo LED
        self.bt_configurar_parpadeo = CTkButton(self.frame, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, border_width = 2,
                hover_color = c_naranjo, fg_color = 'transparent', text = 'Configurar parpadeo LED', height = 20, text_color = c_negro)
        self.bt_configurar_parpadeo.place(relx = 0.5, rely = 0.3, anchor = tkinter.CENTER)

        #Boton Volver
        self.bt_volver = CTkButton(self.frame, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, border_width = 2,
                hover_color = c_naranjo, fg_color = 'transparent', text = 'Volver', height = 30, text_color = c_negro)
        self.bt_volver.place(relx = 0.9, rely = 0.1, anchor = tkinter.CENTER)

        #Boton ingresar
        self.bt_guardar_cambios = CTkButton(self.frame, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, border_width = 2,
                hover_color = c_naranjo, fg_color = 'transparent', text = 'Guardar cambios', height = 60, text_color = c_negro)
        self.bt_guardar_cambios.place(relx = 0.5, rely = 0.9, anchor = tkinter.CENTER)

        #Boton Modificar PIN de seguridad
        self.bt_modificar_pin = CTkButton(self.frame, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, border_width = 2,
                hover_color = c_naranjo, fg_color = 'transparent', text = 'Modificar PIN de seguridad', height = 20, text_color = c_negro)
        self.bt_modificar_pin.place(relx = 0.5, rely = 0.7, anchor = tkinter.CENTER)

        #Boton Restablecer ajustes de fábrica
        self.bt_restablecer_ajustes = CTkButton(self.frame, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, border_width = 2,
                hover_color = c_naranjo, fg_color = 'transparent', text = 'Restablecer ajustes de fábrica', height = 20, text_color = c_negro)
        self.bt_restablecer_ajustes.place(relx = 0.9, rely = 0.7, anchor = tkinter.CENTER)

        #ComboBox Volumen buzzers
        self.cb_volumen_buzzers = customtkinter.CTkComboBox(self.frame, values=["1", "2", "3"], border_color = c_negro, fg_color = c_blanco, button_color = c_negro, button_hover_color = c_naranjo,
                                                    text_color = c_negro, dropdown_fg_color = c_blanco,dropdown_hover_color = c_naranjo, dropdown_text_color = c_negro)
        self.cb_volumen_buzzers.place(relx = 0.1, rely = 0.5, anchor = tkinter.CENTER)

        #ComboBox Duracion de alarma
        self.cb_duracion_alarma = customtkinter.CTkComboBox(self.frame, values=["1", "2", "3"], border_color = c_negro, fg_color = c_blanco, button_color = c_negro, button_hover_color = c_naranjo,
                                                    text_color = c_negro, dropdown_fg_color = c_blanco,dropdown_hover_color = c_naranjo, dropdown_text_color = c_negro)
        self.cb_duracion_alarma.place(relx = 0.1, rely = 0.7, anchor = tkinter.CENTER)

        #ComboBox Fuente de las letras
        self.cb_fuente_letras = customtkinter.CTkComboBox(self.frame, values=["1", "2", "3"], border_color = c_negro, fg_color = c_blanco, button_color = c_negro, button_hover_color = c_naranjo,
                                                    text_color = c_negro, dropdown_fg_color = c_blanco,dropdown_hover_color = c_naranjo, dropdown_text_color = c_negro)
        self.cb_fuente_letras.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

        #SwitchButton Sistema de sensores
        self.switch_var = customtkinter.StringVar(value="on")
        self.sw_sistema_sensores = customtkinter.CTkSwitch(self.frame, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, text = 'Sistema sensores',
                                                    variable = self.switch_var, text_color = c_negro, fg_color = c_naranjo, onvalue="on", offvalue="off")
        self.sw_sistema_sensores.place(relx = 0.9, rely = 0.3, anchor = tkinter.CENTER)

configuracion = configuracion()
configuracion.mainloop()