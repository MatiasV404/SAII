import os
from PIL import Image
import customtkinter
from customtkinter import *
import tkinter
import sys
import subprocess

#Rutas de acceso
menu_ruta = os.path.join(os.path.dirname(os.path.realpath(__file__)))

class perfil(customtkinter.CTk):
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

                #Columnas y filas
                self.columnconfigure(3, weight = 5)
                self.rowconfigure(3, weight = 5)
                
                #Signo de exclamacion y posicion
                self.signo_exclamacion = customtkinter.CTkLabel(self, image = self.signo_exclamacion, text = '', fg_color = c_blanco)
                self.signo_exclamacion.place(relx = 0.1, rely = 0.1, anchor = tkinter.NE)
                
                #Texto Perfil
                self.texto_pefil = customtkinter.CTkLabel(master = self, width=200, height = 100, corner_radius=0, font = ('sans rerif', 75), fg_color = c_blanco,
                                                        text_color = c_negro, text = "Perfil")
                self.texto_pefil.place(relx = 0.42, rely = 0.05)

                #Boton Perfil
                self.bt_perfil = CTkButton(self, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, border_width = 3,
                        hover_color = c_gris, fg_color = c_blanco, text = 'Perfil', height = 20, width = 100, text_color = c_negro)
                self.bt_perfil.place(relx = 0.9, rely = 0.1, anchor = tkinter.CENTER)

                #Boton Cerrar sesión
                self.bt_cerrar = CTkButton(self, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, border_width = 3,
                        hover_color = c_gris, fg_color = c_blanco, text = 'Cerrar sesión', height = 20, width = 100, text_color = c_negro, command = self.accesoLogin)
                self.bt_cerrar.place(relx = 0.9, rely = 0.15, anchor = tkinter.CENTER)

                #Boton Volver
                self.bt_volver = CTkButton(self.frame, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, border_width = 3, width = 100,
                        hover_color = c_gris, fg_color = 'transparent', text = 'Volver', height = 30, text_color = c_negro, command = self.accesoMenu)
                self.bt_volver.place(relx = 0.075, rely = 0.25, anchor = tkinter.CENTER)

                #Boton Cambiar contraseña
                self.bt_cambiar_contrasenia = CTkButton(self.frame, font = customtkinter.CTkFont('sans rerif', 15), border_color = c_negro, border_width = 3,
                        hover_color = c_gris, fg_color = 'transparent', text = 'Cambiar contraseña', height = 30, width = 200, text_color = c_negro)
                self.bt_cambiar_contrasenia.place(relx = 0.5, rely = 0.7, anchor = tkinter.CENTER)

                #Boton Eliminar cuenta
                self.bt_eliminar_cuenta = CTkButton(self.frame, font = customtkinter.CTkFont('sans rerif', 15), border_color = c_negro, border_width = 3,
                        hover_color = c_gris, fg_color = 'transparent', text = 'Eliminar cuenta', height = 30, width = 197, text_color = c_negro)
                self.bt_eliminar_cuenta.place(relx = 0.5, rely = 0.8, anchor = tkinter.CENTER)

        #Funcion que accede de perfil a menu
        def accesoMenu(self):
                ruta_acceso = os.path.join(menu_ruta, "menu.py")
                self.withdraw()
                try:
                        subprocess.run([sys.executable, ruta_acceso])
                        self.destroy() #deiconfy recupera la ventana que se cerro con withdraw
                except Exception as e:
                        print(f"Error al ejecutar el otro script: {e}")
        
        #Funcion que accede de cerrar sesion a login
        def accesoLogin(self):
                ruta_acceso = os.path.join(menu_ruta, "login.py")
                self.withdraw()
                try:
                        subprocess.run([sys.executable, ruta_acceso])
                        self.destroy() #deiconfy recupera la ventana que se cerro con withdraw
                except Exception as e:
                        print(f"Error al ejecutar el otro script: {e}")

perfil = perfil()

def mostrarPerfil():
        perfil.mainloop()
        
mostrarPerfil()