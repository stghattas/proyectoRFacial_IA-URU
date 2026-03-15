import cv2
from PIL import Image, ImageTk

def convertir_frame_a_tkinter(frame):
    """
    Convierte un frame de OpenCV (BGR) a un objeto PhotoImage
    que Tkinter puede renderizar en pantalla.
    """
    # OpenCV usa BGR por defecto, Tkinter necesita RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame_rgb)
    return ImageTk.PhotoImage(image=img)

def dibujar_overlay(frame, texto_persona, emocion, confianza):
    """
    Dibuja un panel oscuro y texto superpuesto en el frame de video.
    """
    alto, ancho = frame.shape[:2]
    
    texto_identidad = f"Identificado: {texto_persona}"
    texto_emocion = f"Emocion: {emocion} ({confianza:.1f}%)"
    
    # Dibujar un rectángulo semi-transparente/oscuro en la parte inferior para que resalte el texto
    # Coordenadas: (x1, y1), (x2, y2)
    cv2.rectangle(frame, (10, alto - 80), (450, alto - 10), (0, 0, 0), -1)
    
    # Escribir el texto sobre el rectángulo
    cv2.putText(frame, texto_identidad, (20, alto - 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    cv2.putText(frame, texto_emocion, (20, alto - 20), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
    
    return frame