import os
import tkinter
from PIL import Image
from tkinter import ttk
from customtkinter import CTk, CTkFrame, CTkEntry, CTkLabel, CTkButton, CTkImage, CTkComboBox
import customtkinter

# Ruta del directorio de imágenes
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'images')

# Definición de colores
c_blanco = '#FFFFFF'
c_negro = '#010101'
c_naranjo = '#FF8000'

# Creación de la ventana principal
root = CTk()
root.geometry('1280x720+320+180')
root.minsize(1280, 720)
root.config(bg=c_blanco)
root.title('Registrar Usuario')

# Carga de la imagen de la llama
logo_llama = CTkImage(Image.open(os.path.join(image_path, 'llama.png')), size=(120, 120))

# Creación del marco principal
frame = CTkFrame(root, fg_color=c_blanco)
frame.grid(column=3, row=3, sticky='nsew', padx=50, pady=50)

root.columnconfigure(3, weight=5)
root.rowconfigure(3, weight=5)

# Logo y posición
logo = CTkLabel(frame, image=logo_llama, text='')
logo.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

# Etiquetas para los campos
etiqueta_usuario = CTkLabel(frame, text_color=c_negro, text="Ingresar nombre de usuario", font=('sans-serif', 12),
                            fg_color=c_blanco)
etiqueta_usuario.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)

etiqueta_contrasenia = CTkLabel(frame, text_color=c_negro, text="Ingresar contraseña", font=('sans-serif', 12),
                                fg_color=c_blanco)
etiqueta_contrasenia.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

etiqueta_confirmar_contraseña = CTkLabel(frame, text_color=c_negro, text="Confirmar contraseña",
                                          font=('sans-serif', 12), fg_color=c_blanco)
etiqueta_confirmar_contraseña.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

etiqueta_email = CTkLabel(frame, text_color=c_negro, text="Ingresar correo electrónico", font=('sans-serif', 12),
                          fg_color=c_blanco)
etiqueta_email.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)

etiqueta_pregunta_seguridad = CTkLabel(frame, text_color=c_negro, text="Escoja una pregunta de seguridad",
                                       font=('sans-serif', 12), fg_color=c_blanco)
etiqueta_pregunta_seguridad.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)

etiqueta_respuesta_seguridad = CTkLabel(frame, text_color=c_negro, text="Respuesta a la pregunta de seguridad",
                                        font=('sans-serif', 12), fg_color=c_blanco)
etiqueta_respuesta_seguridad.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)

# Entrada campos
user = CTkEntry(frame, font=('sans-serif', 12), placeholder_text='Nombre de usuario',
                border_color=c_negro, fg_color=c_blanco, width=220, height=40)
user.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

contrasenia = CTkEntry(frame, font=('sans-serif', 12), placeholder_text='Contraseña',
                      border_color=c_negro, fg_color=c_blanco, width=220, height=40)
contrasenia.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

confirmar_contraseña = CTkEntry(frame, font=('sans-serif', 12), placeholder_text='Confirmar contraseña',
                                border_color=c_negro, fg_color=c_blanco, width=220, height=40)
confirmar_contraseña.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

email = CTkEntry(frame, font=('sans-serif', 12), placeholder_text='Correo electronico',
                 border_color=c_negro, fg_color=c_blanco, width=220, height=40)
email.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

# Menú desplegable para la pregunta de seguridad
preguntas_seguridad = ["¿Nombre de tu primera mascota?", "¿Lugar de nacimiento?", "¿Nombre de tu mejor amigo/a?"]
pregunta_seguridad_combobox = CTkComboBox(frame, corner_radius=5, values=preguntas_seguridad, font=('sans-serif', 12),
                                          width=220)
pregunta_seguridad_combobox.set("Selecciona una pregunta")
pregunta_seguridad_combobox.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

# Campo para la respuesta a la pregunta de seguridad
respuesta_seguridad = CTkEntry(frame, font=('sans-serif', 12), placeholder_text='Respuesta a la pregunta de seguridad',
                              border_color=c_negro, fg_color=c_blanco, width=220, height=40)
respuesta_seguridad.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

# Boton volver
bt_volver = CTkButton(frame, font=customtkinter.CTkFont('sans-serif', 12), border_color=c_negro, border_width=2,
                      hover_color=c_naranjo, fg_color='transparent', text='Volver', width=100, height=40, text_color=c_negro)
bt_volver.place(relx=0.45, rely=0.9, anchor=tkinter.CENTER)

# Boton registrar
bt_registrar = CTkButton(frame, font=customtkinter.CTkFont('sans-serif', 12), border_color=c_negro, border_width=2,
                        hover_color=c_naranjo, fg_color='transparent', text='Registrar', width=100, height=40, text_color=c_negro)
bt_registrar.place(relx=0.55, rely=0.9, anchor=tkinter.CENTER)

# Inicia el bucle principal de la interfaz gráfica
root.mainloop()
