import os
from PIL import Image
import customtkinter
from customtkinter import *
import tkinter
from tkinter import PhotoImage
import sys
import subprocess

menu_ruta = os.path.join(os.path.dirname(os.path.realpath(__file__)))

class historialActividad(customtkinter.CTk):
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
        
        #Texto Historial de Actividad
        self.texto_historial_actividad = customtkinter.CTkLabel(master = self, width=300, height = 100, font = ('sans rerif', 50), fg_color = c_blanco,
                                                    bg_color = c_blanco, text_color = c_negro, text = "Historial de actividad")
        self.texto_historial_actividad.place(relx = 0.35, rely = 0.05)

        #Signo de exclamacion y posicion
        self.signo_exclamacion = customtkinter.CTkLabel(self, image = self.signo_exclamacion, text = '', fg_color = c_blanco)
        self.signo_exclamacion.place(relx = 0.1, rely = 0.1, anchor = tkinter.NE)

        #Boton Volver
        self.bt_volver = CTkButton(self, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, border_width = 3,
                hover_color = c_gris, fg_color = c_blanco, text = 'Volver', height = 20, width = 100, text_color = c_negro, command = self.accesoMenu)
        self.bt_volver.place(relx = 0.9, rely = 0.1, anchor = tkinter.CENTER)

        #Tabla historial de actividad
        self.tab_historial_actividad = customtkinter.CTkTabview(self, width = 1000, height = 450, border_width = 2, fg_color = c_blanco)
        self.tab_historial_actividad.place(relx = 0.1, rely = 0.3)

        self.scroll = customtkinter.CTkScrollableFrame(self.tab_historial_actividad)

        '''
        #Scrollbar Tabla hisotorial de actividad
        self.
        '''
    #Funcion que retorna al menú
    def accesoMenu(self):
        ruta_acceso = os.path.join(menu_ruta, "menu.py")
        self.withdraw()
        try:
                subprocess.run([sys.executable, ruta_acceso])
                self.destroy() #deiconfy recupera la ventana que se cerro con withdraw
        except Exception as e:
                print(f"Error al ejecutar el otro script: {e}")


historialActividad = historialActividad()

def mostrarHistorialActividad():
    historialActividad.mainloop()

mostrarHistorialActividad()