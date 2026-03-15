import tkinter as tk
import sys

from models.database import DatabaseManager
from models.ai_engine import AIEngine
from views.main_window import MainWindow

from controllers.registro_ctrl import RegistroController
from controllers.gestion_ctrl import GestionController
from controllers.deteccion_ctrl import DeteccionController
from controllers.reportes_ctrl import ReportesController

def main():
    root = tk.Tk()
    root.title("Sistema de Reconocimiento Facial y Análisis de Emociones")
    root.geometry("1050x700")

    print("Inicializando Base de Datos...")
    db = DatabaseManager()
    
    print("Cargando motor de Inteligencia Artificial (Esto puede tomar unos segundos)...")
    ai = AIEngine()

    app_view = MainWindow(root)

    ctrl_registro = RegistroController(view=app_view.tab_registro, db=db, ai=ai)
    ctrl_gestion = GestionController(view=app_view.tab_gestion, db=db)
    ctrl_deteccion = DeteccionController(view=app_view.tab_deteccion, db=db, ai=ai, root=root)
    ctrl_reportes = ReportesController(view=app_view.tab_reportes, db=db)

    # ==========================================
    # LOGICA DE CIERRE LIMPIO
    # ==========================================
    def al_cerrar():
        print("\nCerrando el sistema de forma segura...")
        # 1. Asegurarnos de apagar la cámara y liberar el hardware
        ctrl_deteccion.detener_camara()
        
        # 2. Destruir la ventana de Tkinter
        root.destroy()
        
        # 3. Forzar el fin del proceso de Python para liberar la terminal
        sys.exit(0)

    # Interceptar el clic en la "X" de la ventana para ejecutar nuestra función
    root.protocol("WM_DELETE_WINDOW", al_cerrar)

    print("¡Sistema listo! Abriendo interfaz...")
    root.mainloop()

if __name__ == "__main__":
    main()