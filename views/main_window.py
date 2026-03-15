import tkinter as tk
from tkinter import ttk

from views.tab_registro import TabRegistro
from views.tab_gestion import TabGestion
from views.tab_deteccion import TabDeteccion
from views.tab_reportes import TabReportes

class MainWindow:
    def __init__(self, root):
        self.root = root
        
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)

        # 1. Crear los marcos (frames) EXACTAMENTE una vez
        self.frame_registro = ttk.Frame(self.notebook)
        self.frame_gestion = ttk.Frame(self.notebook)
        self.frame_deteccion = ttk.Frame(self.notebook)
        self.frame_reportes = ttk.Frame(self.notebook)

        # 2. Añadirlos al Notebook (Pestañas)
        self.notebook.add(self.frame_registro, text='Registro de Personas')
        self.notebook.add(self.frame_gestion, text='Gestión y Privacidad')
        self.notebook.add(self.frame_deteccion, text='Detección en Tiempo Real')
        self.notebook.add(self.frame_reportes, text='Reportes')

        # 3. Inicializar el contenido de cada pestaña
        self.tab_registro = TabRegistro(self.frame_registro)
        self.tab_gestion = TabGestion(self.frame_gestion)
        self.tab_deteccion = TabDeteccion(self.frame_deteccion)
        self.tab_reportes = TabReportes(self.frame_reportes)