"""Modelo de datos para una canción o tono de alarma."""

from dataclasses import dataclass
from pathlib import Path


@dataclass
class Song:
    """Representa una canción subida o disponible en la aplicación."""

    id: str
    title: str
    file_path: Path
