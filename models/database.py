import sqlite3
import json
import numpy as np
from datetime import datetime
from config import DB_PATH

class DatabaseManager:
    def __init__(self):
        # check_same_thread=False permite que los hilos de la cámara consulten la BD
        self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        # Tabla de Personas
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS personas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                embedding TEXT NOT NULL
            )
        ''')
        # Tabla de Historial
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS detecciones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                persona_id INTEGER,
                emocion TEXT,
                confianza REAL,
                fecha_hora TEXT,
                FOREIGN KEY(persona_id) REFERENCES personas(id)
            )
        ''')
        self.conn.commit()

    def registrar_persona(self, nombre, apellido, email, embedding_vector):
        """Guarda un nuevo usuario y su vector facial."""
        try:
            emb_json = json.dumps(embedding_vector.tolist())
            self.cursor.execute(
                "INSERT INTO personas (nombre, apellido, email, embedding) VALUES (?, ?, ?, ?)",
                (nombre, apellido, email, emb_json)
            )
            self.conn.commit()
            return True, "Registro exitoso."
        except sqlite3.IntegrityError:
            return False, "Error: El email ya está registrado."
        except Exception as e:
            return False, f"Error inesperado: {str(e)}"

    def obtener_todas_las_personas(self):
        """Devuelve una lista de diccionarios con los datos y embeddings cargados como numpy arrays."""
        self.cursor.execute("SELECT id, nombre, apellido, embedding FROM personas")
        filas = self.cursor.fetchall()
        personas = []
        for fila in filas:
            personas.append({
                "id": fila[0],
                "nombre": fila[1],
                "apellido": fila[2],
                "embedding": np.array(json.loads(fila[3]))
            })
        return personas

    def guardar_deteccion(self, persona_id, emocion, confianza):
        """Registra una detección en el historial."""
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute(
            "INSERT INTO detecciones (persona_id, emocion, confianza, fecha_hora) VALUES (?, ?, ?, ?)",
            (persona_id, emocion, confianza, fecha_actual)
        )
        self.conn.commit()

    def obtener_estadisticas_emociones(self):
        """Devuelve un conteo de cuántas veces se ha detectado cada emoción."""
        self.cursor.execute("SELECT emocion, COUNT(*) FROM detecciones GROUP BY emocion")
        return self.cursor.fetchall()