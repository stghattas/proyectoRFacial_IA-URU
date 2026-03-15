🎭 Sistema de Reconocimiento Facial y Análisis de Emociones <br>

Este proyecto es un sistema integral desarrollado para la materia de Inteligencia Artificial. Utiliza técnicas de Visión Artificial y Redes Neuronales Profundas para identificar personas registradas y analizar su estado emocional en tiempo real.

🚀 Características Principales <br>

- Registro Biométrico: Captura y almacenamiento de embeddings faciales (vectores matemáticos) mediante el modelo Facenet.

- Detección en Tiempo Real: Identificación de usuarios con overlay informativo en video.

- Análisis Emocional: Clasificación de 7 emociones básicas (Felicidad, Tristeza, Enojo, Sorpresa, Neutral, Miedo, Disgusto).

- Panel de Gestión (CRUD): Administración de usuarios registrados con un sistema de "Spoiler de Privacidad" para visualizar rostros.

- Estadísticas e Historial: Reportes gráficos de las emociones detectadas utilizando Matplotlib.

- Arquitectura Modular: Separación estricta de responsabilidades (Modelos, Vistas y Controladores).

🛠️ Tecnologías Utilizadas <br>

Lenguaje: Python 3.10.11

IA & Visión: DeepFace (TensorFlow/Keras backend) y OpenCV.

Interfaz Gráfica: Tkinter (GUI Nativa de Python).

Base de Datos: SQLite3 (Persistencia local).

Gráficos: Matplotlib.

📦 Instalación y Configuración <br>

Sigue estos pasos para replicar el entorno de desarrollo:

1. Clonar el repositorio <br>

`git clone https://github.com/tu-usuario/proyectoRFacial_IA-URU.git` <br>

`cd proyectoRFacial_IA-URU` <br>

2. Configurar el Entorno Virtual (Recomendado) <br>

Es crucial utilizar Python 3.10 para asegurar la compatibilidad con TensorFlow: <br>

`python -m venv env_facial` <br>

`.\env_facial\Scripts\activate` <br>

3. Instalar Dependencias

`pip install -r requirements.txt` <br>

`pip install tf-keras` <br>

📂 Estructura del Proyecto <br>
├── models/         # Lógica de IA (DeepFace) y Base de Datos (SQLite) <br>
├── views/          # Componentes de la Interfaz Gráfica (Tkinter) <br>
├── controllers/    # Orquestadores que unen la lógica con la vista <br>
├── utils/          # Funciones auxiliares de cámara e imagen <br>
├── rostros/        # Almacenamiento local de fotos (Ignorado por Git) <br>
├── config.py       # Configuraciones globales y umbrales <br>
└── main.py         # Punto de entrada de la aplicación <br>

🔒 Privacidad y Seguridad
Este proyecto implementa buenas prácticas de seguridad de datos biométricos:

Exclusión de Datos: El archivo .gitignore está configurado para no subir la base de datos (.db) ni las fotografías físicas (rostros/) al repositorio público.

Spoiler de Rostro: En el panel de gestión, las imágenes están ocultas por defecto para proteger la privacidad visual del usuario.

📝 Uso
Ejecuta el sistema con python main.py.

En la pestaña Registro, ingresa tus datos y captura tu rostro.

En la pestaña Detección, inicia la cámara para comenzar el análisis en vivo.

Consulta la pestaña Reportes para ver las estadísticas de uso.

Hecho por: <br>

⭐ Samer Ghattas - Estudiante de Ingeniería en Computación.