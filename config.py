import os

# Rutas del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "sistema_facial.db")

# Configuracion de la IA
UMBRAL_RECONOCIMIENTO = 10.0  # Umbral de distancia euclidiana para Facenet

# Mapeo de emociones (Ingles a Español según requerimiento)
EMOTION_MAP = {
    'happy': 'Felicidad',
    'sad': 'Tristeza',
    'angry': 'Enojo',
    'surprise': 'Sorpresa',
    'neutral': 'Neutral',
    'fear': 'Miedo',
    'disgust': 'Disgusto'
}