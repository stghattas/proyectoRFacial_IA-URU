import tkinter as tk
from tkinter import ttk

class TabGestion:
    def __init__(self, parent_frame):
        self.frame = parent_frame
        self._construir_interfaz()

    def _construir_interfaz(self):
        # Frame izquierdo para la tabla
        frame_tabla = ttk.LabelFrame(self.frame, text="Personas Registradas")
        frame_tabla.pack(side='left', fill='both', expand=True, padx=10, pady=10)

        columnas = ('id', 'nombre', 'apellido', 'email')
        self.tree = ttk.Treeview(frame_tabla, columns=columnas, show='headings')
        self.tree.heading('id', text='ID')
        self.tree.heading('nombre', text='Nombre')
        self.tree.heading('apellido', text='Apellido')
        self.tree.heading('email', text='Email')
        
        self.tree.column('id', width=30)
        self.tree.pack(fill='both', expand=True, padx=5, pady=5)

        # Botones de acción debajo de la tabla
        frame_botones = ttk.Frame(frame_tabla)
        frame_botones.pack(pady=5)
        self.btn_actualizar = ttk.Button(frame_botones, text="Actualizar Lista")
        self.btn_actualizar.grid(row=0, column=0, padx=5)
        self.btn_eliminar = ttk.Button(frame_botones, text="Eliminar Seleccionado")
        self.btn_eliminar.grid(row=0, column=1, padx=5)

        # Frame derecho para la privacidad (Spoiler de foto)
        frame_foto = ttk.LabelFrame(self.frame, text="Privacidad de Rostro")
        frame_foto.pack(side='right', fill='y', padx=10, pady=10)

        self.lbl_foto = tk.Label(frame_foto, text="🔒\nFoto Oculta\n(Seleccione un registro)", bg='gray', fg='white', width=30, height=15)
        self.lbl_foto.pack(padx=10, pady=10)

        self.btn_spoiler = ttk.Button(frame_foto, text="👁️ Mostrar Foto (Spoiler)", state='disabled')
        self.btn_spoiler.pack(pady=5)

    def asignar_comandos(self, cmd_actualizar, cmd_eliminar, cmd_spoiler, cmd_seleccionar):
        self.btn_actualizar.config(command=cmd_actualizar)
        self.btn_eliminar.config(command=cmd_eliminar)
        self.btn_spoiler.config(command=cmd_spoiler)
        self.tree.bind('<<TreeviewSelect>>', cmd_seleccionar)

    def obtener_seleccion(self):
        seleccion = self.tree.selection()
        if not seleccion: return None
        item = self.tree.item(seleccion[0])
        return item['values'] # Devuelve [id, nombre, apellido, email]