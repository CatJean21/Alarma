"""Modelo de datos para una alarma."""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Alarm:
    """Representa una alarma configurada por el usuario."""

    id: str
    hour: int
    minute: int
    label: str = "Alarma"
    enabled: bool = True
    days: List[str] = field(default_factory=list)
    song_id: Optional[str] = None
