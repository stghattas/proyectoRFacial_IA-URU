import numpy as np
from deepface import DeepFace
# Importamos la configuración global desde la raíz
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import EMOTION_MAP, UMBRAL_RECONOCIMIENTO

class AIEngine:
    def extraer_embedding(self, frame):
        """Extrae el embedding facial usando Facenet."""
        try:
            # enforce_detection=True lanza error si no hay un rostro claro
            res = DeepFace.represent(frame, model_name="Facenet", enforce_detection=True)
            return np.array(res[0]["embedding"])
        except ValueError:
            return None # No se detectó rostro

    def analizar_emocion(self, frame):
        """Analiza la emoción dominante y devuelve su traducción y nivel de confianza."""
        try:
            res = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=True, silent=True)
            emocion_en = res[0]['dominant_emotion']
            confianza = res[0]['emotion'][emocion_en]
            
            emocion_es = EMOTION_MAP.get(emocion_en, emocion_en)
            return emocion_es, confianza
        except ValueError:
            return None, 0.0

    def buscar_persona(self, embedding_actual, lista_personas):
        """Calcula la distancia Euclidiana para encontrar coincidencias en la BD."""
        if embedding_actual is None or not lista_personas:
            return None

        mejor_coincidencia = None
        menor_distancia = float('inf')

        for persona in lista_personas:
            distancia = np.linalg.norm(embedding_actual - persona["embedding"])
            if distancia < menor_distancia:
                menor_distancia = distancia
                mejor_coincidencia = persona

        if menor_distancia < UMBRAL_RECONOCIMIENTO:
            return mejor_coincidencia
        return None