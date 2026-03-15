import cv2
from tkinter import messagebox

class RegistroController:
    def __init__(self, view, db, ai):
        self.view = view
        self.db = db
        self.ai = ai

        # Conectar el botón de la vista con el método de este controlador
        self.view.asignar_comando_registro(self.procesar_registro)

    def procesar_registro(self):
        # 1. Obtener datos de la vista
        datos = self.view.obtener_datos()
        
        if not all(datos.values()):
            messagebox.showwarning("Campos incompletos", "Por favor, llene todos los campos.")
            return

        # 2. Capturar 1 frame de la cámara
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()

        if not ret:
            messagebox.showerror("Error de Cámara", "No se pudo acceder a la cámara web.")
            return

        # 3. Procesar con Inteligencia Artificial
        embedding = self.ai.extraer_embedding(frame)
        if embedding is None:
            messagebox.showerror("Error", "No se detectó ningún rostro. Asegúrese de estar bien iluminado.")
            return
        
        # 4. Verificar duplicados (Buscar en la BD si el rostro ya existe)
        personas_db = self.db.obtener_todas_las_personas()
        duplicado = self.ai.buscar_persona(embedding, personas_db)
        
        if duplicado:
             messagebox.showerror("Error", f"Esta persona ya está registrada como: {duplicado['nombre']} {duplicado['apellido']}")
             return

        # 5. Guardar en Base de Datos
        exito, msj = self.db.registrar_persona(
            datos['nombre'], 
            datos['apellido'], 
            datos['email'], 
            embedding
        )
        
        # 6. Actualizar Vista según el resultado
        if exito:
            messagebox.showinfo("Éxito", msj)
            self.view.limpiar_formulario()
        else:
            messagebox.showerror("Error DB", msj)