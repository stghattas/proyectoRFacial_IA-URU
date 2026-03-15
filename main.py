import tkinter as tk
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Importar Modelos
from models.database import DatabaseManager
from models.ai_engine import AIEngine

# Importar Vista Principal
from views.main_window import MainWindow

# Importar Controladores
from controllers.registro_ctrl import RegistroController
from controllers.deteccion_ctrl import DeteccionController
from controllers.reportes_ctrl import ReportesController

def main():
    # 1. Inicializar la ventana base de Tkinter
    root = tk.Tk()
    root.title("Sistema de Reconocimiento Facial y Análisis de Emociones")
    root.geometry("1050x700") # Un poco más ancho para dar espacio a las pestañas

    # 2. Instanciar los Modelos (Lógica pura y Base de datos)
    print("Inicializando Base de Datos...")
    db = DatabaseManager()
    
    print("Cargando motor de Inteligencia Artificial (Esto puede tomar unos segundos)...")
    ai = AIEngine()

    # 3. Instanciar la Vista Principal (Interfaz)
    app_view = MainWindow(root)

    # 4. Instanciar los Controladores (El "puente" entre la UI y los Modelos)
    # Les pasamos la pestaña correspondiente y los modelos que necesitan
    ctrl_registro = RegistroController(view=app_view.tab_registro, db=db, ai=ai)
    ctrl_deteccion = DeteccionController(view=app_view.tab_deteccion, db=db, ai=ai, root=root)
    ctrl_reportes = ReportesController(view=app_view.tab_reportes, db=db)

    print("¡Sistema listo! Abriendo interfaz...")
    
    # 5. Iniciar el bucle infinito de la interfaz gráfica
    root.mainloop()

if __name__ == "__main__":
    main()