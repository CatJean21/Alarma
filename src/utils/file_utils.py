"""Helpers para validación y manejo de archivos de audio."""

from pathlib import Path

from src.config import SUPPORTED_AUDIO_FORMATS


def is_supported_audio(file_path: Path) -> bool:
    """Devuelve True si la extensión del archivo corresponde a un audio soportado."""
    return file_path.suffix.lower() in SUPPORTED_AUDIO_FORMATS
