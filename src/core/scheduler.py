"""Planificador encargado de verificar la hora y disparar alarmas."""


class AlarmScheduler:
    """Vigila las alarmas activas y ejecuta una acción cuando coincide la hora."""

    def start(self) -> None:
        """Inicia la vigilancia de alarmas en segundo plano."""
        raise NotImplementedError("Pendiente de implementar")

    def stop(self) -> None:
        """Detiene el planificador de alarmas."""
        raise NotImplementedError("Pendiente de implementar")
