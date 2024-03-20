# virtual_pet
Practica 02 - Python to learn structure of projects with pygame

Structe Project (Convetion as per AI chat gpt)

game_name/
│
├── assets/
│   ├── images/            # Aquí se guardan todas las imágenes del juego
│   ├── sounds/            # Aquí se guardan todos los efectos de sonido
│   └── fonts/             # Aquí se guardan todas las fuentes de texto
│
├── data/                  # Carpeta para cualquier otro tipo de datos necesarios (como archivos de configuración)
│
├── src/                   # Carpeta que contiene el código fuente del juego
│   ├── main.py            # Archivo principal del juego (donde se inicia el juego)
│   ├── player.py          # Clase para el jugador
│   ├── enemy.py           # Clase para los enemigos
│   ├── level.py           # Clase para los niveles
│   └── helpers.py         # Funciones de utilidad y helpers
│
├── docs/                  # Documentación del juego (opcional)
│
└── README.md              # Documentación general del juego


Vamos a desarollarlo con esta esctrucrura para llevar una mejor convencion del mismo

ClassName : Clases
funciones_class : Funciones de clases
variables_all : Variables dentro de las clases, funciones

folder_name : formato de nombrar carpeteas
file_name : formato de nombrar archivos


Windows:

Crea el entorno virtual para descargar los config/requirements.txt

python -m venv env

env/bin/activate

pip install -r requirements.txt (ubicate en config)

