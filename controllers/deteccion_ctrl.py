import cv2
import threading
from tkinter import messagebox
from utils.camera_utils import convertir_frame_a_tkinter

class DeteccionController:
    def __init__(self, view, db, ai, root):
        self.view = view
        self.db = db
        self.ai = ai
        self.root = root 

        self.cap = None
        self.detectando = False
        self.personas_db = []
        
        # NUEVA VARIABLE: Nuestro "semáforo" para la IA
        self.ia_procesando = False 

        self.view.asignar_comandos(self.iniciar_camara, self.detener_camara)

    def iniciar_camara(self):
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            messagebox.showerror("Error", "No se pudo iniciar la cámara.")
            return

        self.detectando = True
        self.view.cambiar_estado_botones(True)
        self.personas_db = self.db.obtener_todas_las_personas() 
        self.procesar_video()

    def detener_camara(self):
        self.detectando = False
        if self.cap:
            self.cap.release()
        self.view.cambiar_estado_botones(False)

    def procesar_video(self):
        if self.detectando and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                # 1. SOLO enviamos el frame a la IA si NO está ocupada
                if not self.ia_procesando:
                    self.ia_procesando = True # Ponemos el semáforo en rojo
                    threading.Thread(
                        target=self.analizar_frame_ia, 
                        args=(frame.copy(),), 
                        daemon=True
                    ).start()

                # 2. El video se sigue mostrando de forma fluida y sin lag
                imgtk = convertir_frame_a_tkinter(frame)
                self.view.actualizar_frame(imgtk)

            self.root.after(30, self.procesar_video)

    def analizar_frame_ia(self, frame):
        try:
            embedding = self.ai.extraer_embedding(frame)
            
            if embedding is not None:
                persona = self.ai.buscar_persona(embedding, self.personas_db)
                emocion, confianza = self.ai.analizar_emocion(frame)
                
                if persona:
                    texto_persona = f"{persona['nombre']} {persona['apellido']}"
                    self.db.guardar_deteccion(persona['id'], emocion, confianza)
                else:
                    texto_persona = "No Registrada"

                texto_mostrar = f"Identificado: {texto_persona} | Emoción: {emocion} ({confianza:.1f}%)"
                self.view.actualizar_info(texto_mostrar)
        finally:
            # 3. IMPORTANTE: Liberamos la IA (semáforo en verde) pase lo que pase
            self.ia_procesando = False