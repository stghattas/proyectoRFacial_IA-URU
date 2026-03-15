import tkinter as tk
from tkinter import ttk
# Importaremos las pestañas a medida que las vayamos creando
from views.tab_registro import TabRegistro
from views.tab_deteccion import TabDeteccion
# from views.tab_reportes import TabReportes

class MainWindow:
    def __init__(self, root):
        self.root = root
        
        # Configuración del sistema de pestañas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)

        # Crear los marcos (frames) para cada pestaña
        self.frame_registro = ttk.Frame(self.notebook)
        self.frame_deteccion = ttk.Frame(self.notebook)
        # self.frame_reportes = ttk.Frame(self.notebook)

        # Añadir los marcos al Notebook
        self.notebook.add(self.frame_registro, text='Registro de Personas')
        self.notebook.add(self.frame_deteccion, text='Detección en Tiempo Real')
        # self.notebook.add(self.frame_reportes, text='Reportes')

        # Inicializar el contenido de cada pestaña
        self.tab_registro = TabRegistro(self.frame_registro)
        self.tab_deteccion = TabDeteccion(self.frame_deteccion)
        # self.tab_reportes = TabReportes(self.frame_reportes)