import tkinter as tk
from tkinter import ttk

class TabDeteccion:
    def __init__(self, parent_frame):
        self.frame = parent_frame
        self._construir_interfaz()

    def _construir_interfaz(self):
        # Etiqueta donde se mostrará el video en tiempo real
        self.lbl_video = tk.Label(self.frame)
        self.lbl_video.pack(pady=10)

        # Panel de controles
        frame_controles = ttk.Frame(self.frame)
        frame_controles.pack(pady=10)

        # Botones (Los comandos se asignarán desde el controlador)
        self.btn_iniciar = ttk.Button(frame_controles, text="Iniciar Cámara")
        self.btn_iniciar.grid(row=0, column=0, padx=10)

        self.btn_detener = ttk.Button(frame_controles, text="Detener", state='disabled')
        self.btn_detener.grid(row=0, column=1, padx=10)

        # Etiqueta para mostrar la información detectada de forma rápida
        self.lbl_info = ttk.Label(self.frame, text="Esperando detección...", font=('Arial', 14))
        self.lbl_info.pack(pady=10)

    # -------------------------------------------------------------
    # Métodos para que el Controlador actualice esta vista
    # -------------------------------------------------------------
    def actualizar_frame(self, imgtk):
        """Recibe una imagen en formato Tkinter y la actualiza en la etiqueta."""
        self.lbl_video.imgtk = imgtk
        self.lbl_video.configure(image=imgtk)

    def actualizar_info(self, texto):
        """Actualiza el texto inferior con el nombre y la emoción."""
        self.lbl_info.config(text=texto)

    def cambiar_estado_botones(self, detectando):
        """Alterna qué botones están clickeables según el estado."""
        if detectando:
            self.btn_iniciar.config(state='disabled')
            self.btn_detener.config(state='normal')
        else:
            self.btn_iniciar.config(state='normal')
            self.btn_detener.config(state='disabled')
            self.lbl_video.config(image='') # Limpia el último frame
            self.lbl_info.config(text="Cámara detenida.")

    def asignar_comandos(self, cmd_iniciar, cmd_detener):
        """Conecta los clics de los botones con las funciones del controlador."""
        self.btn_iniciar.config(command=cmd_iniciar)
        self.btn_detener.config(command=cmd_detener)