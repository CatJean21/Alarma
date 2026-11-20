"""Reproductor de audio para sonar y detener canciones de alarma."""

from pathlib import Path


class AudioPlayer:
    """Interfaz base para reproducir y detener archivos de audio."""

    def play(self, file_path: Path) -> None:
        """Reproduce el archivo de audio indicado."""
        raise NotImplementedError("Pendiente de implementar con tu librería de audio")

    def stop(self) -> None:
        """Detiene la reproducción actual."""
        raise NotImplementedError("Pendiente de implementar con tu librería de audio")
