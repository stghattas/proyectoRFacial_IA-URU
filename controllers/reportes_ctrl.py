import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox

class ReportesController:
    def __init__(self, view, db):
        self.view = view
        self.db = db
        self.canvas_widget = None

        # Conectar el botón de la vista con el método de actualización
        self.view.asignar_comando_actualizar(self.generar_grafico)

        # Generar el gráfico por primera vez al iniciar
        self.generar_grafico()

    def generar_grafico(self):
        # 1. Obtener datos de la base de datos
        datos = self.db.obtener_estadisticas_emociones()
        
        if not datos:
            # Si no hay datos, no intentamos dibujar el gráfico
            return

        # Separar las tuplas en dos listas para matplotlib
        emociones = [fila[0] for fila in datos]
        cantidades = [fila[1] for fila in datos]

        # 2. Crear la figura de Matplotlib
        fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
        colores = ['#4CAF50', '#2196F3', '#F44336', '#FFC107', '#9C27B0', '#795548', '#607D8B']
        
        # Generar gráfico de barras
        ax.bar(emociones, cantidades, color=colores[:len(emociones)])
        ax.set_title('Frecuencia de Emociones Detectadas')
        ax.set_xlabel('Emociones')
        ax.set_ylabel('Cantidad de Detecciones')
        
        # Rotar las etiquetas del eje X para que se lean bien
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
        fig.tight_layout() # Ajustar márgenes

        # 3. Incrustar en Tkinter
        frame_destino = self.view.obtener_frame_grafico()
        
        # Si ya existía un gráfico anterior, lo eliminamos para no superponerlos
        if self.canvas_widget:
            self.canvas_widget.destroy()

        # Dibujar el nuevo canvas
        canvas = FigureCanvasTkAgg(fig, master=frame_destino)
        canvas.draw()
        self.canvas_widget = canvas.get_tk_widget()
        self.canvas_widget.pack(fill='both', expand=True)