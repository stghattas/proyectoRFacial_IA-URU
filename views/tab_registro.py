import tkinter as tk
from tkinter import ttk

class TabRegistro:
    def __init__(self, parent_frame):
        self.frame = parent_frame
        self._construir_interfaz()

    def _construir_interfaz(self):
        # Contenedor principal del formulario
        frame_form = ttk.LabelFrame(self.frame, text="Datos Personales")
        frame_form.pack(pady=20, padx=20, fill='x')

        # Campos del formulario
        ttk.Label(frame_form, text="Nombre:").grid(row=0, column=0, padx=5, pady=10)
        self.entry_nombre = ttk.Entry(frame_form)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=10)

        ttk.Label(frame_form, text="Apellido:").grid(row=0, column=2, padx=5, pady=10)
        self.entry_apellido = ttk.Entry(frame_form)
        self.entry_apellido.grid(row=0, column=3, padx=5, pady=10)

        ttk.Label(frame_form, text="Email:").grid(row=0, column=4, padx=5, pady=10)
        self.entry_email = ttk.Entry(frame_form)
        self.entry_email.grid(row=0, column=5, padx=5, pady=10)

        # Botón de registro (El comando se asignará desde el controlador)
        self.btn_capturar = ttk.Button(self.frame, text="Capturar Rostro y Registrar")
        self.btn_capturar.pack(pady=15)

    # Métodos para que el controlador pueda leer y limpiar los datos
    def obtener_datos(self):
        return {
            "nombre": self.entry_nombre.get().strip(),
            "apellido": self.entry_apellido.get().strip(),
            "email": self.entry_email.get().strip()
        }

    def limpiar_formulario(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_apellido.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

    def asignar_comando_registro(self, comando):
        """Asigna la función que se ejecutará al presionar el botón."""
        self.btn_capturar.config(command=comando)