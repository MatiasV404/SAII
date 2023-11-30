import os
import tkinter as tk
from PIL import Image
from customtkinter import CTk, CTkFrame, CTkEntry, CTkLabel, CTkButton, CTkImage, CTkComboBox
import customtkinter
import subprocess,sys

menu_ruta = os.path.join(os.path.dirname(os.path.realpath(__file__)))
class RegistroUsuarioApp(CTk):
    def __init__(self):
        super().__init__()

        # Ruta del directorio de imágenes
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'images')

        # Definición de colores
        c_blanco = '#FFFFFF'
        c_negro = '#010101'
        c_naranjo = '#FF8000'

        # Configuración de la ventana principal
        self.geometry('1280x720+320+180')
        self.minsize(1280, 720)
        self.config(bg=c_blanco)
        self.title('Registrar Usuario')

        # Creación del marco principal
        self.frame = CTkFrame(self, fg_color=c_blanco)
        self.frame.grid(column=3, row=3, sticky='nsew', padx=50, pady=50)

        self.columnconfigure(3, weight=5)
        self.rowconfigure(3, weight=5)

        # Logo y posición
        logo_llama = CTkImage(Image.open(os.path.join(image_path, 'llama.png')), size=(120, 120))
        self.logo = CTkLabel(self.frame, image=logo_llama, text='')
        self.logo.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        # Etiquetas para los campos
        self.etiqueta_usuario = CTkLabel(self.frame, text_color=c_negro, text="Ingresar nombre de usuario", font=('sans-serif', 12),
                                         fg_color=c_blanco)
        self.etiqueta_usuario.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

        self.etiqueta_contrasenia = CTkLabel(self.frame, text_color=c_negro, text="Ingresar contraseña", font=('sans-serif', 12),
                                             fg_color=c_blanco)
        self.etiqueta_contrasenia.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

        self.etiqueta_confirmar_contraseña = CTkLabel(self.frame, text_color=c_negro, text="Confirmar contraseña",
                                                       font=('sans-serif', 12), fg_color=c_blanco)
        self.etiqueta_confirmar_contraseña.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

        self.etiqueta_email = CTkLabel(self.frame, text_color=c_negro, text="Ingresar correo electrónico", font=('sans-serif', 12),
                                       fg_color=c_blanco)
        self.etiqueta_email.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

        self.etiqueta_pregunta_seguridad = CTkLabel(self.frame, text_color=c_negro, text="Escoja una pregunta de seguridad",
                                                    font=('sans-serif', 12), fg_color=c_blanco)
        self.etiqueta_pregunta_seguridad.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

        self.etiqueta_respuesta_seguridad = CTkLabel(self.frame, text_color=c_negro, text="Respuesta a la pregunta de seguridad",
                                                     font=('sans-serif', 12), fg_color=c_blanco)
        self.etiqueta_respuesta_seguridad.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

        # Entrada campos
        self.user = CTkEntry(self.frame, font=('sans-serif', 12), placeholder_text='Nombre de usuario',
                             border_color=c_negro, fg_color=c_blanco, width=220, height=40)
        self.user.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        self.contrasenia = CTkEntry(self.frame, font=('sans-serif', 12), placeholder_text='Contraseña',
                                   border_color=c_negro, fg_color=c_blanco, width=220, height=40)
        self.contrasenia.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.confirmar_contraseña = CTkEntry(self.frame, font=('sans-serif', 12), placeholder_text='Confirmar contraseña',
                                             border_color=c_negro, fg_color=c_blanco, width=220, height=40)
        self.confirmar_contraseña.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.email = CTkEntry(self.frame, font=('sans-serif', 12), placeholder_text='Correo electronico',
                              border_color=c_negro, fg_color=c_blanco, width=220, height=40)
        self.email.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        # Menú desplegable para la pregunta de seguridad
        preguntas_seguridad = ["¿Nombre de tu primera mascota?", "¿Lugar de nacimiento?", "¿Nombre de tu mejor amigo/a?"]
        self.pregunta_seguridad_combobox = CTkComboBox(self.frame, corner_radius=5, values=preguntas_seguridad, font=('sans-serif', 12),
                                                       width=220)
        self.pregunta_seguridad_combobox.set("Selecciona una pregunta")
        self.pregunta_seguridad_combobox.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        # Campo para la respuesta a la pregunta de seguridad
        self.respuesta_seguridad = CTkEntry(self.frame, font=('sans-serif', 12),
                                           placeholder_text='Respuesta a la pregunta de seguridad',
                                           border_color=c_negro, fg_color=c_blanco, width=220, height=40)
        self.respuesta_seguridad.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

        # Boton volver
        self.bt_volver = CTkButton(self.frame, font=customtkinter.CTkFont('sans-serif', 12), border_color=c_negro, border_width=2,
                                   hover_color=c_naranjo, fg_color='transparent', text='Volver', width=100, height=40, text_color=c_negro,  command = self.login)
        self.bt_volver.place(relx=0.45, rely=0.9, anchor=tk.CENTER)

        # Boton registrar
        self.bt_registrar = CTkButton(self.frame, font=customtkinter.CTkFont('sans-serif', 12), border_color=c_negro, border_width=2,
                                     hover_color=c_naranjo, fg_color='transparent', text='Registrar', width=100, height=40, text_color=c_negro, command = self.accesoMenu)
        self.bt_registrar.place(relx=0.55, rely=0.9, anchor=tk.CENTER)

    #Funcion que retorna al login
    def login(self):
        ruta_acceso = os.path.join(menu_ruta, "login.py")
        self.withdraw()
        try:
                subprocess.run([sys.executable, ruta_acceso])
                self.destroy() #deiconfy recupera la ventana que se cerro con withdraw
        except Exception as e:
                print(f"Error al ejecutar el otro script: {e}")

    #Funcion que retorna al menu
    def accesoMenu(self):
        ruta_acceso = os.path.join(menu_ruta, "menu.py")
        self.withdraw()
        try:
                subprocess.run([sys.executable, ruta_acceso])
                self.destroy() #deiconfy recupera la ventana que se cerro con withdraw
        except Exception as e:
                print(f"Error al ejecutar el otro script: {e}")
       

if __name__ == "__main__":
    registro_usuario_app = RegistroUsuarioApp()
    registro_usuario_app.mainloop()
