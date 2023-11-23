from customtkinter import *

# Definición de colores
c_blanco = '#FFFFFF'
c_negro = '#010101'
c_naranjo = '#FF8000'

def on_button_click(value):
    """
    Función llamada cuando se hace clic en los botones numéricos y de retroceso.
    """
    current_text = entry.get()
    if value == '←':
        entry.delete(len(current_text) - 1)
    elif len(current_text) < 4:
        entry.insert("insert", str(value))

def close_window():
    """Función llamada cuando se hace clic en el botón de cerrar ('X')."""
    root.destroy()

# Configuración de la ventana principal
root = CTk()
root.geometry('1280x720+320+180')
root.minsize(1280, 720)
root.config(bg=c_blanco)
root.title('PIN')

# Marco principal que cubre el input y los botones
main_frame = CTkFrame(root, fg_color=c_blanco)
main_frame.pack(expand=True, pady=20)

# Marco que contiene el input y el título "PIN"
entry_frame = CTkFrame(main_frame, fg_color=("black", "lightgray"))
entry_frame.grid(row=1, column=0, columnspan=3, pady=(0, 10))

# Título "PIN" centrado arriba del input
title_label = CTkLabel(entry_frame, text="PIN", text_color='white', font=('Arial', 30), bg_color="black")
title_label.grid(row=0, column=0, columnspan=3, pady=(20, 0))

# Botón de cierre en la esquina superior derecha
close_button = CTkButton(entry_frame, text='X', font=('Arial', 16), border_color=c_blanco, fg_color=c_negro, command=close_window)
close_button.grid(row=0, column=2, sticky='ne', pady=(20, 0), padx=(0, 10))

# Input para el PIN
entry = CTkEntry(entry_frame, font=('Arial', 24), border_color=c_negro, fg_color=c_blanco, width=480, show='*')
entry.grid(row=1, column=0, columnspan=3, pady=(0, 10))  # Añadí espacio debajo del input

# Botones numéricos y de retroceso
buttons = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9',
    '←', '0', '✓',
]

# Marco que cubre los botones
frame_border = CTkFrame(entry_frame, bg_color='black')
frame_border.grid(row=2, column=0, columnspan=3, pady=(0, 10), padx=10, sticky='nsew')

row_val = 0
col_val = 0

for button in buttons:
    CTkButton(frame_border, text=button, font=('Arial', 18), fg_color=("black", "lightgray"),
              command=lambda b=button: on_button_click(b)).grid(row=row_val, column=col_val, padx=10, pady=10)
    col_val += 1
    if col_val > 2:
        col_val = 0
        row_val += 1

# Iniciar la aplicación
root.mainloop()
