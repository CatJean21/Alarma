"""Gestor de alarmas (crear, editar, activar/desactivar y eliminar)."""

from typing import List

from src.models import Alarm


class AlarmManager:
    """Coordina las operaciones sobre las alarmas del usuario."""

    def __init__(self) -> None:
        self._alarms: List[Alarm] = []

    def list_alarms(self) -> List[Alarm]:
        """Devuelve la lista de alarmas registradas."""
        return list(self._alarms)

    def add_alarm(self, alarm: Alarm) -> None:
        """Agrega una nueva alarma."""
        self._alarms.append(alarm)

    def remove_alarm(self, alarm_id: str) -> bool:
        """Elimina una alarma por su identificador."""
        initial_count = len(self._alarms)
        self._alarms = [a for a in self._alarms if a.id != alarm_id]
        return len(self._alarms) < initial_count
