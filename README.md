# Alarma

Aplicación de escritorio en Python para gestionar alarmas con canciones personalizadas subidas por el usuario.

## Estructura del proyecto

```text
Alarma/
├── main.py                      # Punto de entrada de la aplicación
├── requirements.txt             # Dependencias de Python
├── src/                         # Código fuente principal
│   ├── config.py                # Rutas, constantes y configuración general
│   ├── models/                  # Modelos de datos (Alarm, Song)
│   ├── core/                    # Lógica de negocio (gestor y planificador de alarmas)
│   ├── audio/                   # Subida/importación y reproducción de canciones
│   ├── storage/                 # Persistencia local (JSON / SQLite)
│   ├── ui/                      # Interfaz gráfica de escritorio
│   │   ├── main_window.py       # Ventana principal
│   │   ├── views/               # Pantallas (alarmas, biblioteca de canciones)
│   │   └── components/          # Widgets y componentes reutilizables
│   └── utils/                   # Utilidades de archivos y validaciones
├── data/                        # Datos locales de la aplicación
│   ├── alarms.json              # Registro de alarmas guardadas
│   └── songs/                   # Canciones subidas por el usuario (ignoradas en Git)
├── assets/                      # Recursos estáticos de la app
│   ├── icons/                   # Iconos de la interfaz
│   └── default_sounds/          # Tonos de alarma incluidos por defecto
└── tests/                       # Pruebas unitarias
```

## Inicio rápido

1. Crea y activa un entorno virtual:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. Instala las dependencias que vayas agregando en `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta la aplicación:
   ```bash
   python main.py
   ```

   ni idea de que hago
