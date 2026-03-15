import tkinter as tk
from tkinter import ttk

class TabReportes:
    def __init__(self, parent_frame):
        self.frame = parent_frame
        self._construir_interfaz()

    def _construir_interfaz(self):
        ttk.Label(self.frame, text="Estadísticas de Emociones", font=('Arial', 16, 'bold')).pack(pady=20)
        
        # Frame vacío diseñado específicamente para alojar el gráfico de Matplotlib
        self.frame_grafico = ttk.Frame(self.frame)
        self.frame_grafico.pack(fill='both', expand=True, padx=20, pady=10)

        # Botón para refrescar los datos desde la base de datos
        self.btn_actualizar = ttk.Button(self.frame, text="Actualizar Gráficos")
        self.btn_actualizar.pack(pady=10)

    def asignar_comando_actualizar(self, comando):
        """Asigna la función que genera el gráfico al presionar el botón."""
        self.btn_actualizar.config(command=comando)
        
    def obtener_frame_grafico(self):
        """Devuelve el contenedor para que el controlador incruste el canvas de Matplotlib."""
        return self.frame_grafico