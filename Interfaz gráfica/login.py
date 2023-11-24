from customtkinter import *
from tkinter import PhotoImage
import customtkinter
import os
import tkinter
from PIL import Image

class login(customtkinter.CTk):
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
        self.maxsize(1280,720)
        self.title('S.A.I.I')

        #Imagenes
        self.logo_llama = customtkinter.CTkImage(Image.open(os.path.join(image_path,'llama.png')), size = (200, 200))
        self.signo_exclamacion = customtkinter.CTkImage(Image.open(os.path.join(image_path,'signoExclamacion.png')), size = (100, 50))

        self.frame = CTkFrame(self, fg_color = c_blanco)
        self.frame.grid(column = 3, row = 3, sticky = 'nsew')

        self.columnconfigure(3, weight = 5)
        self.rowconfigure(3, weight = 5)
        
        #Texto Iniciar sesion
        self.texto_iniciar = customtkinter.CTkTextbox(master = self, width=600, height = 100, corner_radius=0, font = ('sans rerif', 100), fg_color = c_blanco,
                                                      text_color = c_negro)
        self.texto_iniciar.place(relx = 0.3, rely = 0.05) 
        self.texto_iniciar.insert("0.0", "Iniciar sesión" * 1)
        self.texto_iniciar.configure(state = DISABLED)

        #Texto Olvidaste tu contraseña
        self.texto_olvidaste = customtkinter.CTkTextbox(master = self, width=300, height = 25, corner_radius=0, font = ('sans rerif', 12), fg_color = c_blanco,
                                                      bg_color = c_blanco, text_color = c_azul)
        self.texto_olvidaste.place(relx = 0.44, rely = 0.8) 
        self.texto_olvidaste.insert("0.0", "¿Olvidaste tu contraseña?" * 1)
        self.texto_olvidaste.configure(state = DISABLED)

        #Logo y posicion
        self.logo = customtkinter.CTkLabel(self, image = self.logo_llama, text = '', fg_color = c_blanco)
        self.logo.place(relx = 0.5, rely = 0.35, anchor = tkinter.CENTER) 

        #Signo de exclamacion y posicion
        self.signo_exclamacion = customtkinter.CTkLabel(self, image = self.signo_exclamacion, text = '', fg_color = c_blanco)
        self.signo_exclamacion.place(relx = 0.1, rely = 0.1, anchor = tkinter.NE)

        #Entrada correo y contraseña
        self.correo = CTkEntry(self, font = ('sans rerif', 12), placeholder_text = 'Correo electronico',
                        border_color = c_negro, fg_color = c_blanco, width = 220, height = 40)
        self.correo.place(relx = 0.5, rely = 0.6, anchor = tkinter.CENTER)

        self.contrasenia = CTkEntry(self, font = ('sans rerif', 12), placeholder_text = 'Contraseña',
                        border_color = c_negro, fg_color = c_blanco, width = 220, height = 40)
        self.contrasenia.place(relx = 0.5, rely = 0.7, anchor = tkinter.CENTER)

        #Recordar contraseña
        '''
        checkbox = CTkCheckBox(frame, text = '¿Olvidaste tu contraseña?', hover_color = c_naranjo,
                        border_color = c_negro, fg_color = c_naranjo, text_color = c_azul)
        checkbox.place(relx = 0.5, rely = 0.7, anchor = tkinter.CENTER)
        '''
        #Boton ingresar
        self.bt_ingresar = CTkButton(self, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, border_width = 2,
                hover_color = c_naranjo, fg_color = c_blanco, text = 'Ingresar', height = 40, text_color = c_negro)
        self.bt_ingresar.place(relx = 0.5, rely = 0.9, anchor = tkinter.CENTER)

        #Boton registrar usuario
        self.bt_registrar = CTkButton(self, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, border_width = 2,
                hover_color = c_naranjo, fg_color = c_blanco, text = 'registrar usuario', height = 40, text_color = c_negro)
        self.bt_registrar.place(relx = 0.9, rely = 0.9, anchor = tkinter.CENTER)

        #ComboBox Idioma
        self.cb_idioma = customtkinter.CTkComboBox(self.frame, values=["Español", "Inglés"], border_color = c_negro, fg_color = c_blanco, button_color = c_negro, button_hover_color = c_naranjo,
                                                    text_color = c_negro, dropdown_fg_color = c_blanco,dropdown_hover_color = c_naranjo, dropdown_text_color = c_negro)
        self.cb_idioma.place(relx = 0.9, rely = 0.1, anchor = tkinter.CENTER)


login = login()
login.mainloop()
