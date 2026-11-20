"""Repositorio para guardar y cargar alarmas en almacenamiento local."""

from pathlib import Path
from typing import List

from src.config import ALARMS_FILE
from src.models import Alarm


class AlarmRepository:
    """Maneja la lectura y escritura de alarmas (por ejemplo en JSON o SQLite)."""

    def __init__(self, storage_path: Path = ALARMS_FILE) -> None:
        self.storage_path = storage_path

    def load_all(self) -> List[Alarm]:
        """Carga todas las alarmas guardadas."""
        raise NotImplementedError("Pendiente de implementar")

    def save_all(self, alarms: List[Alarm]) -> None:
        """Guarda la lista completa de alarmas."""
        raise NotImplementedError("Pendiente de implementar")
