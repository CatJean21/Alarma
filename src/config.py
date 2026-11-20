"""Configuración general y rutas del proyecto."""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
SONGS_DIR = DATA_DIR / "songs"
ALARMS_FILE = DATA_DIR / "alarms.json"

ASSETS_DIR = BASE_DIR / "assets"
ICONS_DIR = ASSETS_DIR / "icons"
DEFAULT_SOUNDS_DIR = ASSETS_DIR / "default_sounds"

SUPPORTED_AUDIO_FORMATS = (".mp3", ".wav", ".ogg", ".flac")


def ensure_directories() -> None:
    """Crea las carpetas de datos necesarias si aún no existen."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    SONGS_DIR.mkdir(parents=True, exist_ok=True)
