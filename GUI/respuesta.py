import os
from PIL import Image
import customtkinter
from customtkinter import *
import tkinter,sys, subprocess
menu_ruta = os.path.join(os.path.dirname(os.path.realpath(__file__)))
class respuesta(customtkinter.CTk):
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
        
        #Texto Recuperación
        self.texto_recuperacion = customtkinter.CTkLabel(master = self, width=200, height = 100, corner_radius=0, font = ('sans rerif', 60), fg_color = c_blanco,
                                                      bg_color = c_blanco, text_color = c_negro, text = "Recuperación cuenta")
        self.texto_recuperacion.place(relx = 0.30, rely = 0.05)

        #Boton Volver
        self.bt_volver = CTkButton(self, font = customtkinter.CTkFont('sans rerif', 12), border_color = c_negro, border_width = 3,
                hover_color = c_gris, fg_color = c_blanco, text = 'Volver', height = 20, width = 100, text_color = c_negro,command = self.accesoMenu)
        self.bt_volver.place(relx = 0.9, rely = 0.1, anchor = tkinter.CENTER)

         #Texto respuseta
        self.texto_nombre = customtkinter.CTkLabel(master = self, width = 200, height = 30, corner_radius=0, font = ('sans rerif', 15), fg_color = c_blanco,
                                                    bg_color = c_blanco, text_color = c_negro, text = "Responda la pregunta escogida")
        self.texto_nombre.place(relx = 0.42, rely = 0.42) 


        #Entrada respuesta
        self.user = CTkEntry(self, font = ('sans rerif', 12), placeholder_text = '', text_color = c_negro,
                        border_color = c_negro, fg_color = c_blanco, width = 360, height = 40)
        self.user.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)
        
        #Boton Continuar
        self.bt_continuar = CTkButton(self.frame, font = customtkinter.CTkFont('sans rerif', 15), border_color = c_negro, border_width = 3,
                hover_color = c_gris, fg_color = 'transparent', text = 'Continuar', height = 30, width = 197, text_color = c_negro, corner_radius = 3,
                command=self.continuar)
        self.bt_continuar.place(relx = 0.5, rely = 0.6, anchor = tkinter.CENTER)
    #Funcion que retorna 
    def accesoMenu(self):
        ruta_acceso = os.path.join(menu_ruta, "recuperacion.py")
        self.withdraw()
        try:
                subprocess.run([sys.executable, ruta_acceso])
                self.destroy() #deiconfy recupera la ventana que se cerro con withdraw
        except Exception as e:
                print(f"Error al ejecutar el otro script: {e}")
        #Funcion continuar
    def continuar(self):
        ruta_acceso = os.path.join(menu_ruta, "nuevacontrasenia.py")
        self.withdraw()
        try:
                subprocess.run([sys.executable, ruta_acceso])
                self.destroy() #deiconfy recupera la ventana que se cerro con withdraw
        except Exception as e:
                print(f"Error al ejecutar el otro script: {e}")
respuesta = respuesta()
def mostrarRespuesta():
        respuesta.mainloop()

mostrarRespuesta()