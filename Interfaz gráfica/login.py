import os
from PIL import Image
import customtkinter
from customtkinter import *
import tkinter
from tkinter import PhotoImage
import sys
import subprocess

#Rutas de acceso
menu_ruta = os.path.join(os.path.dirname(os.path.realpath(__file__)))

class login(customtkinter.CTk):
        def __init__(self):
                super().__init__()

                image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'images')

                c_blanco = '#FFFFFF'
                c_negro = '#010101'
                c_gris_oscuro = '#424949'
                c_azul = '#0000FF'
                c_gris = '#979A9A'

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

                #Columnas y filas
                self.columnconfigure(3, weight = 5)
                self.rowconfigure(3, weight = 5)
                
                #Texto Iniciar sesion
                self.texto_iniciar = customtkinter.CTkLabel(master = self, width=600, height = 100, corner_radius=0, font = ('sans rerif', 100), fg_color = c_blanco,
                                                        bg_color = c_blanco, text_color = c_negro, text = "Iniciar sesión")
                self.texto_iniciar.place(relx = 0.3, rely = 0.05) 

                #Texto Ingreso de nombre de usuario
                self.texto_nombre = customtkinter.CTkLabel(master = self, width = 200, height = 30, corner_radius=0, font = ('sans rerif', 15), fg_color = c_blanco,
                                                        bg_color = c_blanco, text_color = c_negro, text = "Ingrese su nombre de usuario")
                self.texto_nombre.place(relx = 0.345, rely = 0.525) 

                #Texto Ingreso de contraseña
                self.texto_contraseña = customtkinter.CTkLabel(master = self, width = 200, height = 30, corner_radius=0, font = ('sans rerif', 15), fg_color = c_blanco,
                                                        bg_color = c_blanco, text_color = c_negro, text = "Ingrese su contraseña")
                self.texto_contraseña.place(relx = 0.325, rely = 0.67) 

                #Texto Olvidaste tu contraseña
                self.texto_olvidaste = customtkinter.CTkLabel(master = self, width=200, height = 25, corner_radius=0, font = ('sans rerif', 12), fg_color = c_blanco,
                                                        bg_color = c_blanco, text_color = c_azul, text = "¿Olvidaste tu contraseña")
                self.texto_olvidaste.place(relx = 0.42, rely = 0.8) 

                #Logo y posicion
                self.logo = customtkinter.CTkLabel(self, image = self.logo_llama, text = '', fg_color = c_blanco)
                self.logo.place(relx = 0.5, rely = 0.35, anchor = tkinter.CENTER) 

                #Signo de exclamacion y posicion
                self.signo_exclamacion = customtkinter.CTkLabel(self, image = self.signo_exclamacion, text = '', fg_color = c_blanco)
                self.signo_exclamacion.place(relx = 0.1, rely = 0.1, anchor = tkinter.NE)

                #Entrada correo y contraseña
                self.correo = CTkEntry(self, font = ('sans rerif', 12), placeholder_text = '', text_color = c_negro,
                                border_color = c_negro, fg_color = c_blanco, width = 400, height = 40)
                self.correo.place(relx = 0.5, rely = 0.6, anchor = tkinter.CENTER)

                self.contrasenia = CTkEntry(self, font = ('sans rerif', 12), placeholder_text = '', text_color = c_negro,
                                border_color = c_negro, fg_color = c_blanco, width = 400, height = 40)
                self.contrasenia.place(relx = 0.5, rely = 0.75, anchor = tkinter.CENTER)

                #Boton ingresar
                self.bt_ingresar = CTkButton(self, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, border_width = 2,
                        hover_color = c_gris, fg_color = c_blanco, text = 'Ingresar', height = 40, text_color = c_negro, command = self.accesoMenu)
                self.bt_ingresar.place(relx = 0.5, rely = 0.9, anchor = tkinter.CENTER)

                #Boton registrar usuario
                self.bt_registrar = CTkButton(self, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, border_width = 2,
                        hover_color = c_gris, fg_color = c_blanco, text = 'registrar usuario', height = 40, text_color = c_negro)
                self.bt_registrar.place(relx = 0.9, rely = 0.9, anchor = tkinter.CENTER)

                #ComboBox Idioma
                self.cb_idioma = customtkinter.CTkComboBox(self.frame, values=["Español", "Inglés"], border_color = c_gris_oscuro, fg_color = c_blanco, button_color = c_gris_oscuro, button_hover_color = c_gris,
                                                        text_color = c_negro, dropdown_fg_color = c_blanco,dropdown_hover_color = c_gris, dropdown_text_color = c_negro, bg_color = c_blanco)
                self.cb_idioma.place(relx = 0.9, rely = 0.1, anchor = tkinter.CENTER)

        #Funcion que accede a Menu luego de loggearse
        def accesoMenu(self):
                ruta_acceso = os.path.join(menu_ruta, "menu.py")
                self.withdraw()
                try:
                        subprocess.run([sys.executable, ruta_acceso])
                        self.destroy() #deiconfy recupera la ventana que se cerro con withdraw
                except Exception as e:
                        print(f"Error al ejecutar el otro script: {e}")

login = login()

def mostrarLogin():
        login.mainloop()
mostrarLogin()

