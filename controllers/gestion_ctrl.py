import os
from tkinter import messagebox
from PIL import Image, ImageTk

class GestionController:
    def __init__(self, view, db):
        self.view = view
        self.db = db
        self.mostrando_foto = False
        self.imgtk_actual = None # Para evitar que el recolector de basura de Python borre la imagen

        self.view.asignar_comandos(
            self.cargar_tabla, 
            self.eliminar_registro, 
            self.alternar_spoiler,
            self.al_seleccionar
        )
        self.cargar_tabla()

    def cargar_tabla(self):
        # Limpiar tabla actual
        for item in self.view.tree.get_children():
            self.view.tree.delete(item)
            
        # Cargar de BD
        personas = self.db.obtener_todas_las_personas()
        for p in personas:
            self.view.tree.insert('', 'end', values=(p['id'], p['nombre'], p['apellido'], p['email']))
            
        self._ocultar_foto()

    def eliminar_registro(self):
        datos = self.view.obtener_seleccion()
        if not datos:
            messagebox.showwarning("Atención", "Seleccione una persona de la lista.")
            return
            
        id_persona, email = datos[0], datos[3]
        
        if messagebox.askyesno("Confirmar", f"¿Eliminar a {datos[1]} {datos[2]}?"):
            exito, msj = self.db.eliminar_persona(id_persona)
            if exito:
                # Intentar borrar la foto física
                ruta_foto = os.path.join("rostros", f"{email}.jpg")
                if os.path.exists(ruta_foto):
                    os.remove(ruta_foto)
                self.cargar_tabla()
            else:
                messagebox.showerror("Error", msj)

    def al_seleccionar(self, event):
        """Se activa al hacer clic en un registro de la tabla."""
        self._ocultar_foto()
        self.view.btn_spoiler.config(state='normal')

    def alternar_spoiler(self):
        if self.mostrando_foto:
            self._ocultar_foto()
        else:
            self._mostrar_foto()

    def _mostrar_foto(self):
        datos = self.view.obtener_seleccion()
        if not datos: return
        
        email = datos[3]
        ruta_foto = os.path.join("rostros", f"{email}.jpg")
        
        if os.path.exists(ruta_foto):
            img = Image.open(ruta_foto)
            img = img.resize((250, 200), Image.Resampling.LANCZOS)
            self.imgtk_actual = ImageTk.PhotoImage(image=img)
            self.view.lbl_foto.config(image=self.imgtk_actual, text="", bg='white')
            self.view.btn_spoiler.config(text="🙈 Ocultar Foto")
            self.mostrando_foto = True
        else:
            messagebox.showinfo("Sin Foto", "Este registro es antiguo y no tiene foto guardada.")

    def _ocultar_foto(self):
        self.view.lbl_foto.config(image='', text="🔒\nFoto Oculta", bg='gray')
        self.view.btn_spoiler.config(text="👁️ Mostrar Foto")
        self.mostrando_foto = False