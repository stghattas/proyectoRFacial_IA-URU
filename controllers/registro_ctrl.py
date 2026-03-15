import cv2
import os
from tkinter import messagebox

class RegistroController:
    def __init__(self, view, db, ai):
        self.view = view
        self.db = db
        self.ai = ai
        self.view.asignar_comando_registro(self.procesar_registro)

        # Crear carpeta para guardar las fotos si no existe
        os.makedirs("rostros", exist_ok=True)

    def procesar_registro(self):
        datos = self.view.obtener_datos()
        if not all(datos.values()):
            messagebox.showwarning("Incompleto", "Llene todos los campos.")
            return

        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()

        if not ret:
            messagebox.showerror("Error", "No se pudo acceder a la cámara.")
            return

        embedding = self.ai.extraer_embedding(frame)
        if embedding is None:
            messagebox.showerror("Error", "No se detectó ningún rostro.")
            return
        
        personas_db = self.db.obtener_todas_las_personas()
        duplicado = self.ai.buscar_persona(embedding, personas_db)
        
        if duplicado:
             messagebox.showerror("Error", f"Ya registrada como: {duplicado['nombre']}")
             return

        exito, msj = self.db.registrar_persona(datos['nombre'], datos['apellido'], datos['email'], embedding)
        
        if exito:
            # GUARDAR LA FOTO USANDO EL EMAIL COMO NOMBRE DE ARCHIVO
            ruta_foto = os.path.join("rostros", f"{datos['email']}.jpg")
            cv2.imwrite(ruta_foto, frame)
            
            messagebox.showinfo("Éxito", msj)
            self.view.limpiar_formulario()
        else:
            messagebox.showerror("Error DB", msj)