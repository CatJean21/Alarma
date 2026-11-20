"""Gestor de biblioteca de canciones (subir/importar, listar y eliminar)."""

from pathlib import Path
from typing import List

from src.config import SONGS_DIR
from src.models import Song
from src.utils.file_utils import is_supported_audio


class SongManager:
    """Administra los archivos de audio subidos por el usuario."""

    def __init__(self, songs_dir: Path = SONGS_DIR) -> None:
        self.songs_dir = songs_dir

    def list_songs(self) -> List[Song]:
        """Lista todas las canciones válidas disponibles en la carpeta de canciones."""
        if not self.songs_dir.exists():
            return []

        songs: List[Song] = []
        for path in sorted(self.songs_dir.iterdir()):
            if path.is_file() and is_supported_audio(path):
                songs.append(Song(id=path.stem, title=path.stem, file_path=path))
        return songs

    def upload_song(self, source_path: Path) -> Song:
        """Importa/copia una canción local hacia la carpeta de canciones de la app."""
        raise NotImplementedError("Pendiente de implementar")
