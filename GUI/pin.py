import os
from PIL import Image
from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkImage, CTkEntry
import tkinter as tk
import sys
import subprocess

# Rutas de acceso
menu_ruta = os.path.join(os.path.dirname(os.path.realpath(__file__)))

class RegistroPinApp(CTk):
    def __init__(self):
        super().__init__()

        # Definición de colores
        c_blanco = '#FFFFFF'
        c_negro = '#010101'

        # Configuración de la ventana principal
        self.geometry('1280x720+320+180')
        self.minsize(1280, 720)
        self.config(bg=c_blanco)
        self.title('PIN')

        # Marco principal que cubre el input y los botones
        self.main_frame = CTkFrame(self, fg_color=c_blanco, bg_color = c_blanco)
        self.main_frame.pack(expand=True, pady=20)

        # Marco que contiene el input y el título "PIN"
        self.entry_frame = CTkFrame(self.main_frame, fg_color=("black", "lightgray"))
        self.entry_frame.grid(row=1, column=0, columnspan=3, pady=(0, 10))

        # Título "PIN" centrado arriba del input
        self.title_label = CTkLabel(self.entry_frame, text="PIN", text_color='white', font=('Arial', 30), bg_color="black")
        self.title_label.grid(row=0, column=0, columnspan=3, pady=(20, 0))

        # Botón de cierre en la esquina superior derecha
        self.close_button = CTkButton(self.entry_frame, text='X', font=('Arial', 16), border_color=c_blanco, fg_color=c_negro, command=self.accesoMenu)
        self.close_button.grid(row=0, column=2, sticky='ne', pady=(20, 0), padx=(0, 10))

        # Input para el PIN
        self.entry = CTkEntry(self.entry_frame, font=('Arial', 24), border_color=c_negro, fg_color=c_blanco, width=480, show='*')
        self.entry.grid(row=1, column=0, columnspan=3, pady=(0, 10))  

        # Botones numéricos y de retroceso
        buttons = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            '←', '0', '✓',
        ]

        # Marco que cubre los botones
        frame_border = CTkFrame(self.entry_frame, bg_color='black')
        frame_border.grid(row=2, column=0, columnspan=3, pady=(0, 10), padx=10, sticky='nsew')

        row_val = 0
        col_val = 0

        for button in buttons:
            CTkButton(frame_border, text=button, font=('Arial', 18), fg_color=("black", "lightgray"),
                      command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val, padx=10, pady=10)
            col_val += 1
            if col_val > 2:
                col_val = 0
                row_val += 1

    def on_button_click(self, value):
        current_text = self.entry.get()
        if value == '←':
            self.entry.delete(len(current_text) - 1)
        elif len(current_text) < 4:
            self.entry.insert("insert", str(value))

    #Funcion que retorna al menú
    def accesoMenu(self):
        ruta_acceso = os.path.join(menu_ruta, "menu.py")
        self.withdraw()
        try:
                subprocess.run([sys.executable, ruta_acceso])
                self.destroy() #deiconfy recupera la ventana que se cerro con withdraw
        except Exception as e:
                print(f"Error al ejecutar el otro script: {e}")
if __name__ == "__main__":
    registro_pin_app = RegistroPinApp()
    registro_pin_app.mainloop()

   